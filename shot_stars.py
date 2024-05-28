#! /usr/bin/env python3
# Copyright (c) 2024 <snoopproject@protonmail.com>

import datetime
import os
import requests
import shutil
import signal
import sys
import time
import webbrowser

from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, SpinnerColumn, TimeElapsedColumn, Progress
from rich.table import Table


console = Console()
Windows = True if sys.platform == 'win32' else False
Linux = True if Windows is False else False

console.print("""[yellow]
 ____  _           _     ____  _                 
/ ___|| |__   ___ | |_  / ___|| |_ __ _ _ __ ___ 
\___ \| '_ \ / _ \| __| \___ \| __/ _` | '__/ __|
 ___) | | | | (_) | |_   ___) | || (_| | |  \__ \\
|____/|_| |_|\___/ \__| |____/ \__\__,_|_|  |___/[/yellow]  v0.1, author: https://github.com/snooppr
""")

url_repo = input("Specify the repository url (Github): ")
repo = url_repo.rsplit(sep='/', maxsplit=1)[-1]
repo_api = '/'.join(url_repo.rsplit(sep='/', maxsplit=2)[-2:])

time_start = time.perf_counter()

# Создание каталогов для репозиториев.
if Windows:
    path = os.environ['LOCALAPPDATA'] + f"\\ShotStars\\results\\{repo}"
elif Linux:
    path = os.environ['HOME'] + f"/ShotStars/results/{repo}"
os.makedirs(path, exist_ok=True)


def win_exit():
    """удержание окна консоли скомпилированной версии 'windows_shotstars.exe' для OS Windows."""
    if Windows:
        input("\n'enter' выход")
        sys.exit()


def dif_time():
    """Диапазон прошедшего времени: от последнего сканирования к текущему сканированию."""
    delta = datetime.datetime.today() - datetime.datetime.fromtimestamp(date_file_new)
    return f"{delta.days}d. {(datetime.datetime.utcfromtimestamp(0) + delta).strftime('%Hh. %Mm.')}"


def parsing(diff=False):
    """
    Так как сетевые запросы многократно обращаются к одному хосту,
    то активирована поддержка сессии для поддержания одного,
    но постоянного TCP-соединения (увеличение производительности).
    В случае неудачного подключения или сбоя HTTPAdapter реализует
    автоматически повторные попытки подключения.
    """
    my_session = requests.Session()
    repeat = requests.adapters.HTTPAdapter(max_retries=4)
    my_session.mount('https://', repeat)
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/121.0'}
    try:
        req = my_session.get(f'https://api.github.com/repos/{repo_api}', headers=head, timeout=6)
        r = req.json()
    except Exception:
        console.print('[bold red]Network error![/bold red]')
        win_exit()
        sys.exit()

# Расчет кол-ва страниц для итераций.
# В случае сбоя проверка заголовка 'X-RateLimit-Reset' от сервера на предмет расчета времени до снятия ограничений. 
    try:
        stars = int(r.get("stargazers_count"))
        pages = (stars // 100) + 1
    except Exception:
        console.print("\n[bold red]Attention! The API limit has probably been exceeded, the block will presumably be lifted:",
                      time.strftime('%Y-%m-%d_%H:%M', time.localtime(int(req.headers.get('X-RateLimit-Reset')) + 60)))
        console.print(Panel.fit("Limitations: ~limit 30 requests or 6000 stars/hour", title="Github API"))
        win_exit()
        sys.exit()

# Вывод на печать звезд и описание проекта (если присутствует).
    title_repo = "No repository description available" if r.get('description') is None else r.get('description')
    console.print(f"[green]\n{title_repo}\n[bold green]Github-rating::[/bold green] {stars} stars\n")

# Настройка визуализации прогресса.
    progress = Progress(TimeElapsedColumn(), SpinnerColumn(spinner_name='earth'),
                        "[progress.percentage]{task.percentage:>1.0f}%",
                        BarColumn(bar_width=None, complete_style='yellow', finished_style='cyan yellow'),
                        refresh_per_second=0.4, transient=True)

# Обход и сохранение всех user's, которые ставили звезды репозиторию.
    lst_new = []
    with progress:
        task = progress.add_task("", total=pages)
        for page in range(1, pages+1):
            progress.update(task, advance=1)
            progress.refresh()
            try:
                r = my_session.get(f'https://api.github.com/repos/{repo_api}/stargazers?per_page=100&page={page}',
                                   headers=head, timeout=6).json()
                
                for num in r:
                    lst_new.append(num.get("login"))
            except Exception:
                console.print('\n[bold red]Crash!!')
                win_exit()
                sys.exit()    

    with open(f"{path}/new.txt", "w", encoding="utf-8") as f_w:
        print(*lst_new, file=f_w, sep="\n")

# Сравнение списков пользователей после временных сканирований для обнаружения в них изменений.
    if diff:
        with open(f"{path}/old.txt", "r") as f_r:
            lst_old = f_r.read().split()

        diff_lst_dn = list(set(lst_old) - set(lst_new)) # убывание звезд.
        diff_lst_up = list(set(lst_new) - set(lst_old)) # прибавление звезд.

        if bool(diff_lst_dn) is False:
            console.print("[bold black on white]gone stars not detected")
        if bool(diff_lst_up) is False:
            console.print("[bold black on white]ADDING stars not detected")

        if not any([bool(diff_lst_dn), bool(diff_lst_up)]):
            print('\nfinish', round(time.perf_counter() - time_start, 1), 'sec.') # печать времени исполнения скрипта.
            win_exit()
            sys.exit()
        elif bool(diff_lst_dn) or bool(diff_lst_up):
            per_stars_dn = round(len(diff_lst_dn) * 100 / stars, 2) # расчет % соотношения потерь звезд к общему рейтингу. 
            per_stars_up = round(len(diff_lst_up) * 100 / stars, 2) # расчет % соотношения прибавления звезд к общему рейтингу. 

# Настройка таблиц для вывода на печать в CLI.
            table_dn = Table(title=f"\n[yellow]Gone stars (-{per_stars_dn}%)\nin the last: {dif_time()}[/yellow]",
                             title_justify="center", header_style='yellow', style="yellow")
            table_dn.row_styles = ["none", "dim"]
            table_dn.add_column("N", justify="left", style="yellow", no_wrap=True)
            table_dn.add_column("gone stars", justify="left", style="yellow", no_wrap=True)

            table_up = Table(title=f"\n[cyan]New stars (+{per_stars_up}%)\nin the last: {dif_time()}[/cyan]",
                             title_justify="center", header_style='cyan', style="cyan")
            table_up.row_styles = ["none", "dim"]
            table_up.add_column("N", justify="left", style="cyan", no_wrap=True)
            table_up.add_column("new stars", justify="left", style="cyan", no_wrap=True)

# Сохранение/открытие HTML-отчета/печать CLI-таблиц с результатами, если такие имеются.
            with open(f"{path}/report.html", "w", encoding="utf-8") as file_html:
                file_html.write(f"<!DOCTYPE html>\n<html lang='en'>\n\n<head>\n<title>💫({repo}) HTML-reeport</title>\n" + \
                                "<meta charset='utf-8'>\n<style>\n.textcols {white-space: nowrap}\n" + \
                                ".textcols-item {white-space: normal; display: inline-block; width: 48%; " + \
                                "vertical-align: top; background: #fff2e1}\n" + \
                                ".textcols .textcols-item:first-child {margin-right: 4%}\n" + \
                                ".pic {float: right}\n.shad{display: inline-block}\n" + \
                                ".shad:hover{text-shadow: 0px 0px 14px #6495ED; transform: scale(1.1);\n" + \
                                "transition: transform 0.15s}\n</style>\n</head>\n\n<body>\n" + \
                                f"<h2 align='center' style='text-shadow: 0px 0px 13px #84d2ca' >{url_repo}</h2>\n" + \
                                "<div class='textcols'>\n<div class='textcols-item'>\n" + \
                                f"<h4 style='color:#CC3333'>💫 Gone stars (-{per_stars_dn}%):</h4>\n")

                if bool(diff_lst_dn):
                    file_html.write("<ol>")
                    for N, username in enumerate(diff_lst_dn, 1):
                        table_dn.add_row(f"{N}.", f'https://github.com/{username}')
                        file_html.write(f"\n<li><span class='shad'><a target='_blank' " + \
                                        f"href='https://github.com/{username}'>{username}</a></span></li>")
                    file_html.write("\n</ol>\n")

                file_html.write(f"</div>\n\n<div class='textcols-item'>\n<h4 style='color:#32CD32'>" + \
                                f"🌟 New stars (+{per_stars_up}%):</h4>\n")

                if bool(diff_lst_up):
                    file_html.write("<ol>")
                    for N, username in enumerate(diff_lst_up, 1):
                        table_up.add_row(f"{N}.", f'https://github.com/{username}')
                        file_html.write(f"\n<li><span class='shad'><a target='_blank' " + \
                                        f"href='https://github.com/{username}'>{username}</a></span></li>")
                    file_html.write("\n</ol>\n")

                file_html.write("</div>\n</div>\n\n<br>\n<a href='" + \
                                "https://github.com/snooppr/shotstars/tree/main' target='blank'><img src=" + \
                                "https://raw.githubusercontent.com/snooppr/shotstars/main/images/stars.jpg " + \
                                "alt='The program was written for an article competition' width='600' class='pic'></a>\n\n")
                file_html.write("<span style='color:gray; text-shadow: 0px 0px 20px #333333'>" + \
                                "<small><small>╭📅 Changes over the past " + \
                                f"({dif_time()}): <br>├──{date}<br>└──{time.strftime('%Y-%m-%d_%H:%M', time.localtime())}" + \
                                "</small></small></span>\n\n<p style='color: gray'><small><small>" + \
                                "Software developed for a competition<br>©Author: <a href='https://github.com/snooppr' " + \
                                "target='blank'><img align='center' src='https://github.githubassets.com/favicons/favicon.svg' " + \
                                "alt='' height='30' width='30'/>🪙</a><a href='https://yoomoney.ru/to/4100111364257544' " + \
                                "target='blank' title='Was the program useful? Support the developer financially.'>donate" + \
                                "</a></small></small></p>\n\n</body>\n</html>")

            if bool(diff_lst_dn):
                console.print(table_dn)
            if bool(diff_lst_up):
                console.print(table_up)

            webbrowser.open(f"file://{path}/report.html")


    print('\nfinish', round(time.perf_counter() - time_start, 1), 'sec.')

    win_exit()

# Разбор пользовательского ввода url. Обновление списков прошлых сканирований или добавление нового репо в БД.
# Настройка корректного прерывания 'ctrl + c' скрипта относительно разных OS. Вызов основной функции 'parsing()'.
if __name__ == '__main__':
    try:
        if len(url_repo) == 0:
            console.print("[bold red]'enter' -> exit")
        elif len(url_repo) < 18 or 'github.com' not in url_repo:
            console.print("[bold red]Incorrect repository link provided")
            shutil.rmtree(path, ignore_errors=True)
            win_exit()
        elif os.path.exists(f"{path}/new.txt"):
            date_file_new = os.path.getmtime(f"{path}/new.txt")
            date = time.strftime('%Y-%m-%d_%H:%M', time.localtime(date_file_new))
            console.print(f"\nRepository '{repo}' was last checked ->  {date}")
            a = shutil.copy(f"{path}/new.txt", f"{path}/old.txt")
            parsing(diff=True)
        else:
            console.print(f"\n[bold green]A new repository has been added to the tracking database: '{repo}'.\n" + \
                          "On subsequent/re-scanning of the repository, 'ShotStars' will attempt to calculate stars.")
            parsing()
    except KeyboardInterrupt:
        console.print(f"\n[bold red]Interrupt [italic][/bold red]")
        if Windows:
            os.kill(os.getpid(), signal.SIGBREAK)
        if Linux:
            os.kill(os.getpid(), signal.SIGKILL)
