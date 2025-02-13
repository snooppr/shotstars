#! /usr/bin/env python3
# Copyright (c) 2024 Snooppr <snoopproject@protonmail.com>

import configparser
import datetime
import json
import os
import random
import requests
import shutil
import signal
import sys
import time
import webbrowser

from collections import Counter
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed, TimeoutError
from multiprocessing import active_children, set_start_method
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()
config = configparser.ConfigParser()
image = os.path.join(os.path.dirname(__file__), 'stars.jpg')
Android_lame_workhorse = False
Android = True if hasattr(sys, 'getandroidapilevel') else False
Windows = True if sys.platform == 'win32' else False
Linux = True if Android is False and Windows is False else False


console.print(r"""[yellow]
 ____  _           _     ____  _
/ ___|| |__   ___ | |_  / ___|| |_ __ _ _ __ ___
\___ \| '_ \ / _ \| __| \___ \| __/ _` | '__/ __|
 ___) | | | | (_) | |_   ___) | || (_| | |  \__ \
|____/|_| |_|\___/ \__| |____/ \__\__,_|_|  |___/[/yellow]  v1.8, author: https://github.com/snooppr
""")


# Функции...
def main_cli():
    global url_repo, repo, repo_api, path
    try:
        console.print("Enter [bold green]url[/bold green] (Repository On Github) or '[bold green]history[/bold green]': ",
                      highlight=False, end="")
        url_repo = input("")
    except KeyboardInterrupt:
        console.print(f"\n[bold red][italic]Interrupt[/italic][/bold red]")
        sys.exit()
    repo = url_repo.rsplit(sep='/', maxsplit=1)[-1]
    repo_api = '/'.join(url_repo.rsplit(sep='/', maxsplit=2)[-2:])
    path = path_repo()

    try:
        if url_repo == "history" or url_repo == "his":
            shutil.rmtree(path, ignore_errors=True)
            url_repo, repo, repo_api = his(check_file=True, history=True)
            path = path_repo()
        if len(url_repo) == 0:
            console.print("[bold red]'enter' -> exit")
            win_exit()
        elif len(url_repo) < 18 or 'github.com' not in url_repo:
            console.print("[bold red]Incorrect repository link provided")
            if not os.path.isfile(f"{path}/new.txt"):
                shutil.rmtree(path, ignore_errors=True)
            win_exit()
        elif os.path.exists(f"{path}/new.txt"):
            global date_file_new, date
            date_file_new = os.path.getmtime(f"{path}/new.txt")
            date = time.strftime('%Y-%m-%d_%H:%M', time.localtime(date_file_new))
            d = datetime.datetime.today() - datetime.datetime.fromtimestamp(date_file_new)
            console.print(f"\nRepository '{repo}' was last checked ->  {date} :: ({d.days} days)")
            a = shutil.copy(f"{path}/new.txt", f"{path}/old.txt")
            if os.path.isfile(f"{path}/all_gone_stars.html") is False:
                html_mark(all_stars=f"{path}/all_gone_stars.html")
            if os.path.isfile(f"{path}/all_new_stars.html") is False:
                html_mark(all_stars=f"{path}/all_new_stars.html")
            if os.path.isfile(f"{path}/stars.jpg") is False:
                shutil.copy(image, f"{path}/stars.jpg")
                if Linux: # снятие исполняемого бита для shotstars_cli.bin build версии.
                    os.chmod(f"{path}/stars.jpg", 0o644)
            his()
            check_token()
            parsing(diff=True)
        else:
            console.print(f"\n<[bold magenta]EN[/bold magenta]>[bold green] A new repository has been added to the tracking " + \
                          f"database: '[/bold green][cyan]{repo}[/cyan][bold green]'.\nOn subsequent/re-scanning of the " + \
                          f"repository, 'ShotStars' will attempt to calculate stars.[/bold green]" + \
                          f"\n<[bold magenta]RU[/bold magenta]>[bold green] В БД для отслеживания добавлен новый репозиторий: " + \
                          f"'[/bold green][cyan]{repo}[/cyan][bold green]'.\nПри последующем/повторном сканировании репозитория " + \
                          f"'ShotStars' будет пытаться вычислять звезды.[/bold green]", highlight=False)
            his()
            check_token()
            parsing()
    except KeyboardInterrupt:
        console.print(f"\n[bold red][italic]Interrupt[/italic][/bold red]")
        if Windows:
            os.kill(os.getpid(), signal.SIGBREAK)
        elif Android_lame_workhorse:
            os.kill(os.getpid(), signal.SIGKILL)
        else:
            for child in active_children():
                child.terminate()
                time.sleep(0.06)


def backup_table():
    "Бэкап истории таблицы сканирований, в случае перехода на обновленную версию Shotstars v1.7+."

    if Windows:
        info = f"{path.replace('results' + chr(92) + repo, '')}backup_history.txt"
    else:
        info = f"{path.replace(f'results/{repo}', '')}backup_history.txt"

    console.print(f"\nShotstars [cyan]v1.7[/cyan] has an updated format for the '[cyan]scan table history[/cyan]': " + \
                  f"a '[cyan]stars[/cyan]' column has been added. [bold red]table history will be cleared[/bold red], " + \
                  f"but a backup will be made. You can find the history backup here:\n'" + \
                  f"[cyan]{info}[/cyan]'.", highlight=False)

    with open(f"{path.replace(repo, '')}history.json", "r") as history_urls:
        file = json.load(history_urls)
        url_table_lst = [f"https://github.com/{k}" for k in file]
    with open(info, "w", encoding="utf-8") as backup_history_url:
        backup_history_url.write("Saved urls (backup) that were previously in the Shotstars history table.\n\n")
        backup_history_url.write('\n'.join(url_table_lst))

    os.remove(f"{path.replace(repo, '')}history.json")
    os.execl(sys.executable, sys.executable, *sys.argv)


def his(check_file=False, history=False):
    """История сканирований."""
    if not os.path.isfile(f"{path.replace(repo, '')}history.json"):
        with open(f"{path.replace(repo, '')}history.json", 'w') as not_his_w:
            json.dump({}, not_his_w)
        if check_file:
            console.print("[bold yellow]\nHistory is empty.[/bold yellow]")
            win_exit()

    if history:
        padding = 0 if Android else (0, 1)
        table_his = Table(title=f"\n[bold blue]SCAN HISTORY[/bold blue]",
                          title_justify="center", header_style='bold green', style="bold green", padding=padding, show_lines=True)
        table_his.add_column("N", justify="left", style="bold blue", no_wrap=False)
        table_his.add_column("URL", justify="left", style="magenta", overflow="fold", no_wrap=False)
        table_his.add_column("STARS", justify="left", style="bold yellow", overflow="fold", no_wrap=False)
        table_his.add_column("DATE", justify="center", style="green", no_wrap=False)
        with open(f"{path.replace(repo, '')}history.json", 'r') as his_file:
            his_dict = json.load(his_file)

            dict_urls = {}
            for num, (url, his_date) in enumerate(his_dict.items(), 1):
                try: #In Shotstars version 1.7 the table format has been changed.
                    stars = str(his_date[1])
                except Exception:
                    his_file.close()
                    backup_table()

                his_date = datetime.datetime.fromtimestamp(his_date[0]).strftime('%Y-%m-%d')
                color_repo = url[:url.rfind(url.rsplit(sep='/', maxsplit=1)[-1])] + \
                             f"[bold magenta]{url.rsplit(sep='/', maxsplit=1)[-1]}[/bold magenta]"
                table_his.add_row(str(num), f'https://github.com/{color_repo}', stars, his_date)
                dict_urls[str(num)] = {f'https://github.com/{url}': his_date}

        console.print(table_his)

        console.print("Select url ([bold blue]digit[/bold blue]): ", highlight=False, end="")
        select_his_url = input("")

        try:
            url_repo_glob = list(dict_urls[select_his_url].keys())[0]
        except KeyError:
            console.print("[bold red]not chosen[/bold red]")
            win_exit()
        repo_glob = url_repo_glob.rsplit(sep='/', maxsplit=1)[-1]
        repo_api_glob = '/'.join(url_repo_glob.rsplit(sep='/', maxsplit=2)[-2:])

        return url_repo_glob, repo_glob, repo_api_glob


def path_repo():
    """Создание каталогов для репозиториев."""
    if Windows:
        path = os.environ['LOCALAPPDATA'] + f"\\ShotStars\\results\\{repo}"
    else:
        path = os.environ['HOME'] + f"/ShotStars/results/{repo}"
    os.makedirs(path, exist_ok=True)

    return path


def check_token():
    """Github-token проверка."""
    if not os.path.isfile(f"{path.replace(repo, '')}config.ini"):
        config.add_section('Shotstars')
        config.set('Shotstars', 'token', 'None')
        with open(f"{path.replace(repo, '')}config.ini", 'w') as config_file:
            config.write(config_file)


def win_exit():
    """
    Удержание окна консоли скомпилированной версии 'shotstars_cli.exe' для OS Windows.
    Сначала цветной 'print', потом чистый 'input', иначе прогресс в некоторых случаях может перекрывать сообщение.
    """
    if Windows:
        console.print("\nplease key <ENTER> --> exit")
        input("")

    sys.exit()


def dif_time():
    """
    Диапазон прошедшего времени: от последнего сканирования к текущему сканированию.
    Замена устаревшей функции в Python3.12+: "utcfromtimestamp".
    """
    delta = datetime.datetime.today() - datetime.datetime.fromtimestamp(date_file_new)
    return f"{delta.days}d. {(datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc) + delta).strftime('%Hh. %Mm.')}"


def finish(token, stars=None):
    """Финишное время, проверка наличие/отсутствие токена и заполнение истории сканирований."""
    print('\nfinish', round(time.perf_counter() - time_start, 1), 'sec. in', timeout())

    if token == "None":
        print("Github token not provided.")
    elif token != "None":
        print("Github-token is used!")

    with open(f"{path.replace(repo, '')}history.json", "r") as his_r:
        his_file = json.load(his_r)
        try:
            his_file.update({repo_api: [int(time.time()), stars]})
            his_file = dict(sorted(his_file.items(), key=lambda x: x[1][0], reverse=True))
        except Exception:
            his_r.close()
            backup_table()
    with open(f"{path.replace(repo, '')}history.json", "w") as his_w:
        json.dump(his_file, his_w, indent=1)


def limited(req, token, proc=False):
    """Расчет времени снятия лимита Github-API."""
    headers_time = int(req.headers.get('X-RateLimit-Reset')) + 60
    minut = datetime.datetime.fromtimestamp(headers_time) - datetime.datetime.today()
    minut = int(minut.seconds / 60)
    console.print("\n[bold red]Attention! The API limit has probably been exceeded, the block will presumably be lifted:",
                  time.strftime('%Y-%m-%d_%H:%M', time.localtime(headers_time)), f"::: ({minut} min.)")
    if token == "None":
        console.print(Panel.fit("Limitations: ~limit max '30 requests/hour' or '6000 stars/hour'", title="Github API/No Token"))
    else:
        console.print(Panel.fit("Limitations: ~limit max '500K stars/hour'", title="Github API/Token Used"))

    if proc and not Windows:
        for child in active_children():
            child.terminate()
            time.sleep(0.06)

    win_exit()


def timeout():
    """Местное время когда ПО отработало, если получен лимит, удобно в т.ч. и от него вести отсчет снятия ограничений."""
    date = datetime.datetime.today()
    return f"{date.hour}h:{date.minute}m"


# Функции генерации HTML-кода.
def html_mark(all_stars):
    with open(all_stars, "w", encoding="utf-8") as f_g_his:
        f_g_his.write("""<!DOCTYPE html>\n<html lang='en'>\n\n
<head>
<title> HTML-history</title>
<meta charset='utf-8'>
<style>
.color1 {
 color: #9345a1;
}
.color2 {
 color: #6148e0;
}
.shad{display: inline-block}
.shad:hover{text-shadow: 0px 0px 14px #6495ED; transform: scale(1.1); transition: transform 0.15s}
</style>
</head>
<body style="background-color: #c0c0c0">

<h2 align='center'>_________Total Stars/Date_________</h2>\n""")


def html_rec(file_html, diff_lst, table):
    file_html.write("<ol>")

    for N, username in enumerate(diff_lst, 1):
        table.add_row(f"{N}.", f'https://github.com/{username}')
        file_html.write(f"\n<li><span class='shad'><a target='_blank' " + \
                        f"href='https://github.com/{username}'>{username}</a></span></li>")
    file_html.write("\n</ol>")
    return table


def gener_his_html(diff_lst_dn, html_name, title, stars):
    """Создание html-страниц всей истории сканирований на предмет убывания/прибавления звезд/статистики."""
    with open(html_name, "r", encoding="utf-8") as fr_gone_html:
        f_str = fr_gone_html.read()
        f_lst = f_str.splitlines()
# Суммарный расчет метрик строки заголовка.
        if ' :: ' in f_str:
            date_days_old = f_str.split(sep=":: <span class='color2'>", maxsplit=1)[1].split("_")[0]
            date_all_delta = (datetime.datetime.today() - datetime.datetime.strptime(date_days_old, "%Y-%m-%d")).days
        else:
            date_all_delta = "1 scan"

        all_gone_stars = len(diff_lst_dn)

        for line in f_lst:
            if 'users__' in line:
                dig_tag = line.split(sep='users__', maxsplit=1)[1]
                all_gone_stars += int("".join(dig for dig in list(dig_tag) if dig.isdigit()))

        per_dn_all = round(all_gone_stars * 100 / stars, 2)

        SN = "+" if "new" in html_name else "-"
        S = "🌟" if "new" in html_name else "💫"
        title_gone_stars = title + f"{all_gone_stars} stars ({SN}{per_dn_all}%)␥{date_all_delta} days_________{S}</h2>"

        for i in f_lst:
            if "_________Total" in i:
                index_title = f_lst.index(i)
                f_lst[index_title] = title_gone_stars
            if "</body></html>" in i:
                index_markup = f_lst.index(i)
                f_lst[index_markup] = ''
            if "<h3>Duplicate_Users" in i:
                index_dup = f_lst.index(i)
                f_lst[index_dup] = ''
# Расчет дубликатов пользователей.
    user_his = [user.rsplit("</a></span></li>")[0].rsplit(">", 1)[1] for user in f_lst if "</a></span></li>" in user]
    user_his.extend(diff_lst_dn)
    dup_lst = Counter([i for i in user_his if user_his.count(i) > 1])

    cnt = []
    for k, v in sorted(dup_lst.items(), key=lambda x: x[1], reverse=True):
        cnt.append(f"(<a href='https://github.com/{k}'>{k}</a> ⇔ <i>{v}</i>)")
    str_dup = "<p style='color: #f55700'><h4>None</h4></p>" if bool(cnt) is False else f"<p style='color: #cb2a00'>{'; '.join(cnt)}</p>"


    NG = "New" if "new" in html_name else "Gone"
    with open(html_name, "w", encoding="utf-8") as fw_gone_html:
        fw_gone_html.write('\n'.join(f_lst))
        fw_gone_html.write(f"\n📅 <i>Date Range Of {NG} Stars</i> <b>【<span class='color1'>{dif_time()}</span></b> " + \
                           f":: <span class='color2'>{date} — {time.strftime('%Y-%m-%d_%H:%M', time.localtime())}" + \
                           f"</span><b>】</b> users__<b>{len(diff_lst_dn)}</b>\n<ol>")
        for username in diff_lst_dn:
            fw_gone_html.write(f"\n<li><span class='shad'><a target='_blank' " + \
                               f"href='https://github.com/{username}'>{username}</a></span></li>")

        fw_gone_html.write(f"\n</ol>\n<h3>Duplicate_Users:</h3>{str_dup}")
        fw_gone_html.write("\n</body></html>")


def parsing(diff=False):
    """
    Так как сетевые запросы многократно обращаются к одному хосту, то активирована поддержка сессии для поддержания
    постоянного TCP-соединения (увеличение производительности). В случае неудачного подключения или сбоя HTTPAdapter
    реализует автоматически повторные попытки подключения. Сетевые запросы к API идут параллельно, получение
    результатов по мере поступления, а не по порядку.
    """
    global time_start
    time_start = time.perf_counter()

    my_session = requests.Session()
    repeat = requests.adapters.HTTPAdapter(pool_connections=70, pool_maxsize=60, max_retries=4)
    my_session.mount('https://', repeat)

    config.read(f"{path.replace(repo, '')}config.ini")
    token = config.get('Shotstars', 'token')
    if token != "None":
        head = {'User-Agent': f'Shotstars v1.4', 'Authorization': f'Bearer {token}'}
    elif token == "None":
        head = {'User-Agent': f'Mozilla/5.0 (X11; Linux x86_64; rv:{random.randint(119, 127)}.0) Gecko/20100101 Firefox/121.0'}

    try:
        req = my_session.get(f'https://api.github.com/repos/{repo_api}', headers=head, timeout=6)
        r = req.json()
    except Exception:
        console.print('[bold red]Network error![/bold red]')
        win_exit()

# Расчет кол-ва страниц для итераций.
# В случае сбоя проверка заголовка 'X-RateLimit-Reset' от сервера на предмет расчета времени до снятия ограничений.
    try:
        if r.get('status') or (r.get('message') and "Not Found" in r.get('message')):
            raise ValueError("")
        stars = int(r.get("stargazers_count"))
        pages = (stars // 100) + 1
    except ValueError as err:
        console.print(f"\n[bold red]Check the entered[/bold red] [red]url[/red][bold red], " + \
                      f"it seems that such a repository does not exist:\n<[/bold red] [yellow]{url_repo}[/yellow] " + \
                      f"[bold red]>.[/bold red]", highlight=False)
        if not os.path.isfile(f"{path}/new.txt"):
            shutil.rmtree(path, ignore_errors=True)
        win_exit()
    except Exception:
        limited(req, token)

# Вывод на печать кол-ва звезд, дату создания проекта и описание (если присутствует).
    try:
        size_repo = "N/O" if r.get('size') is None else round(r.get('size') / 1024, 2)
        created_at = "N/O" if r.get('created_at') is None else r.get('created_at').split("T")[0]
        push = "N/O" if r.get('pushed_at') is None else r.get('pushed_at')
        try:
            push_ = datetime.datetime.strptime(push, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d__%H:%M') + "_UTC"
        except Exception:
            push_ = "BAD!"
        title_repo = "No repository description available" if r.get('description') is None else r.get('description')
        console.print(f"\n[cyan]Size::[/cyan] ~ {size_repo} Mb" + \
                      f"\n[cyan]Github-rating::[/cyan] {stars} stars" + \
                      f"\n[cyan]Date-of-creation::[/cyan] {created_at}" + \
                      f"\n[cyan]Date-update (including hidden update)::[/cyan] {push_}" + \
                      f"\n[cyan]Repository-description::[/cyan] {title_repo}\n", highlight=False)
    except Exception:
        console.print('[red]Check Github api (buggy).\nReport issue to developer: "https://github.com/snooppr/shotstars/issues"')
        win_exit()

    if token == "None" and pages > 60:
        console.print("\n[bold yellow][!] Shotstars does not process repositories with stars > 6K+ without a github token " + \
                      "by default.\nUsing a free github token, the limits are significantly increased\n(500K+ stars/hour or " + \
                      "max scanned repository with 40K stars).[/bold yellow]")
        shutil.rmtree(path, ignore_errors=True)
        win_exit()
    elif token != "None" and pages > 400:
        console.print("\n[bold yellow][!] Using a github token, the maximum crawlable repository on Shotstars " + \
                      "is limited to 40K stars.[/bold yellow]")
        shutil.rmtree(path, ignore_errors=True)
        win_exit()

# Обход и сохранение всех user's, которые ставили/снимали звезды репозиторию.
    if Windows:
        tread_max = pages if pages <= (os.cpu_count() * 3) else (os.cpu_count() * 3 if os.cpu_count() <= 36 else 36)
        executor = ThreadPoolExecutor(max_workers=tread_max)
    elif Linux:
        proc_max = pages if pages <= 20 else 20
        executor = ProcessPoolExecutor(max_workers=proc_max)
    elif Android:
        try:
            executor = ProcessPoolExecutor(max_workers=os.cpu_count() * 2)
        except Exception:
            global Android_lame_workhorse
            Android_lame_workhorse = True
            executor = ThreadPoolExecutor(max_workers=8)

    spinner = 'earth' if diff else 'material'
    lst_new, futures = [], {}
    with console.status("[cyan]Working", spinner=spinner):
        for page in range(1, pages+1):
            futures[executor.submit(my_session.get, headers=head, timeout=6,
                                    url=f'https://api.github.com/repos/{repo_api}/stargazers?per_page=100&page={page}')] = None
        try:
            for future in as_completed(futures):
                data = future.result(timeout=12)
                data = data.json()
                for num in data:
                    lst_new.append(num.get("login"))
                futures.pop(future, None)
        except Exception:
            limited(req, token, proc=True)

        try:
            executor.shutdown()
        except Exception:
            pass

    with open(f"{path}/new.txt", "w", encoding="utf-8") as f_w:
        print(*lst_new, file=f_w, sep="\n")

# Сравнение списков пользователей после временных сканирований для обнаружения в них изменений.
    if diff:
        with open(f"{path}/old.txt", "r") as f_r:
            lst_old = f_r.read().split()

        diff_lst_dn = list(set(lst_old) - set(lst_new)) # убывание звезд.
        diff_lst_up = list(set(lst_new) - set(lst_old)) # прибавление звезд.

        if bool(diff_lst_dn) is False:
            console.print("[bold black on white]GONE stars not detected")
        if bool(diff_lst_up) is False:
            console.print("[bold black on white]NEW stars not detected")

        if not any([bool(diff_lst_dn), bool(diff_lst_up)]):
            finish(token, stars)
            win_exit()
        elif bool(diff_lst_dn) or bool(diff_lst_up):
            per_stars_dn = round(len(diff_lst_dn) * 100 / stars, 2) # расчет % соотношения потерь звезд к общему рейтингу.
            per_stars_up = round(len(diff_lst_up) * 100 / stars, 2) # расчет % соотношения прибавления звезд к общему рейтингу.

# Настройка таблиц для вывода на печать в CLI.
            table_dn = Table(title=f"\n[yellow]Gone stars (-{per_stars_dn}%)\nin the last: {dif_time()}[/yellow]",
                             title_justify="center", header_style='yellow', style="yellow", show_lines=True)
            table_dn.row_styles = ["none", "dim"]
            table_dn.add_column("N", justify="left", style="yellow", no_wrap=True)
            table_dn.add_column("GONE STARS", justify="left", style="yellow", no_wrap=False)

            table_up = Table(title=f"\n[cyan]New stars (+{per_stars_up}%)\nin the last: {dif_time()}[/cyan]",
                             title_justify="center", header_style='cyan', style="cyan", show_lines=True)
            table_up.row_styles = ["none", "dim"]
            table_up.add_column("N", justify="left", style="cyan", no_wrap=True)
            table_up.add_column("NEW STARS", justify="left", style="cyan", no_wrap=False)

# Сохранение/открытие HTML-отчета/печать CLI-таблиц с результатами, если такие имеются.
            file_image = f"file://{path}/stars.jpg".replace("\\", "/") if Windows else f"file://{path}/stars.jpg"
            with open(f"{path}/report.html", "w", encoding="utf-8") as file_html:
                file_html.write("<!DOCTYPE html>\n<html lang='en'>\n\n<head>\n" + f"<title>💫({repo}) HTML-report</title>\n" + \
                                "<meta charset='utf-8'>\n<style>\n" + \
                                f"body {{background-image: url('{file_image}'); background-size: cover;\n" + \
"""background-repeat: no-repeat}
.but{display:inline-block; cursor: pointer; font-size:20px; text-decoration:none; padding:10px 20px; color:#2a21db; background:#bec0cc; border-radius:19px; border:2px solid #354251}
.but:hover{background:#354251; color:#ffffff; border:2px solid #354251; transition: all 0.2s ease;}.textcols {white-space: nowrap}
.textcols-item {white-space: normal; display: inline-block; width: 47.7%; vertical-align: top; background: #595c61; opacity: 0.9;}
.textcols .textcols-item:first-child {margin-right: 4.3%}
.donate{white-space: normal; display: inline-block; background: #595c61; opacity: 0.8}
.pic {float: right}
.shad{display: inline-block}
.shad:hover{text-shadow: 0px 0px 14px #6495ED; transform: scale(1.1);
transition: transform 0.15s}
</style>
</head>\n\n<body link="#6cccfb">\n""")
                file_html.write(f"<h2 align='center' style='text-shadow: 0px 0px 13px #84d2ca' >{url_repo}</h2>\n" + \
                                "<div class='textcols'>\n<div class='textcols-item'>\n" + \
                                f"<h4 style='color:#32CD32'>🌟 New stars (+{per_stars_up}%):</h4>\n")

                if bool(diff_lst_up):
                    table_up = html_rec(file_html, diff_lst_up, table_up)

                file_html.write(f"\n<a class='but' href='file://{path}/all_new_stars.html' " + \
                                "title='open all history adding stars'>open all history</a>\n" + \
                                "</div>\n\n<div class='textcols-item'>\n<h4 style='color:#fc3f1d'>" + \
                                f"💫 Gone stars (-{per_stars_dn}%):</h4>\n")

                if bool(diff_lst_dn):
                    table_dn = html_rec(file_html, diff_lst_dn, table_dn)

                file_html.write(f"\n<a class='but' href='file://{path}/all_gone_stars.html' " + \
                                "title='open all history gone stars'>open all history</a>\n" + \
                                "</div>\n</div>\n\n<br>\n<span class='donate' " + \
                                "style='color: white; text-shadow: 0px 0px 20px #333333'>" + \
                                f"<small><small>\n💾 Size:: ~ {size_repo} Mb\n<br>" + \
                                f"✨ Github-rating:: {stars} stars<br>\n⏳ Date-of-creation:: {created_at}<br>\n" + \
                                f"⌛️ Date-update (including hidden update):: {push_}<br>\n" + \
                                f"📖 Repository-description:: {title_repo}</small></small></span><br>\n" + \
                                "<br>\n<span class='donate' style='color: white; text-shadow: 0px 0px 20px #333333'>" + \
                                "<small><small>╭📅 Changes over the past " + \
                                f"({dif_time()}): <br>├──{date}<br>└──{time.strftime('%Y-%m-%d_%H:%M', time.localtime())}" + \
                                "</small></small></span>\n\n<p style='color: white'><small>" + \
                                "Software developed for a competition<br>©Author: <a href='https://github.com/snooppr' " + \
                                "target='blank'><img align='center' src='https://github.githubassets.com/favicons/favicon.svg' " + \
                                "alt='' height='40' width='40'></a></small></p>\n<p class='donate'>\n" + \
                                "<a href='https://yoomoney.ru/to/4100111364257544' target='blank' title='Was the program useful? " + \
                                "Support the developer financially.'>💳 DONATE</a></p>\n\n</body>\n</html>")

# Сохранение/txt-отчета по убывающим звездам на длинной дистанции. Отчеты в CLI-таблицах.
            if bool(diff_lst_dn):
                gener_his_html(diff_lst_dn, html_name=f"{path}/all_gone_stars.html", stars=stars,
                               title = f"<h2 align='center'>💫_________Total Gone Stars/Date ⇢ ")
                console.print(table_dn)

            if bool(diff_lst_up):
                gener_his_html(diff_lst_up, html_name=f"{path}/all_new_stars.html", stars=stars,
                               title = f"<h2 align='center'>🌟_________Total New Stars/Date ↝ ")
                console.print(table_up)

            try:
                webbrowser.open(f"file://{path}/report.html")
            except Exception:
                console.print("[bold red]It is impossible to open the web browser due to problems with the operating system.")

    finish(token, stars)
    win_exit()

# Arbeiten.
if __name__ == '__main__':
    if not Windows:
        set_start_method('fork')
    main_cli()
