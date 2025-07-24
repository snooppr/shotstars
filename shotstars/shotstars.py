#! /usr/bin/env python3
# Copyright (c) 2024 Snooppr <snoopproject@protonmail.com>

import configparser
import datetime
import json
import os
import platform
import plotext as plt_cli
import plotly.graph_objects as plt_html
import random
import re
import requests
import shutil
import signal
import statistics
import subprocess
import sys
import time
import webbrowser

from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
from plotly.offline import get_plotlyjs
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


console = Console()
config = configparser.ConfigParser()
image = os.path.join(os.path.dirname(__file__), 'stars.jpg')
local_tzone = time.tzname[time.localtime().tm_isdst]
Android = True if hasattr(sys, 'getandroidapilevel') else False
Windows = True if sys.platform == 'win32' else False
Linux = True if Android is False and Windows is False else False
__version__ = "v4.5с0"


if os.get_terminal_size().columns > 100 and os.get_terminal_size().lines > 34:
    banner = r"""
   SSSSSSSSSSSSSSS hhhhhhh                                       tttt          
 SS:::::::::::::::Sh:::::h                                    ttt:::t          
S:::::SSSSSS::::::Sh:::::h                                    t:::::t          
S:::::S     SSSSSSSh:::::h                                    t:::::t          
S:::::S             h::::h hhhhh          ooooooooooo   ttttttt:::::ttttttt    
S:::::S             h::::hh:::::hhh     oo:::::::::::oo t:::::::::::::::::t    
 S::::SSSS          h::::::::::::::hh  o:::::::::::::::ot:::::::::::::::::t    
  SS::::::SSSSS     h:::::::hhh::::::h o:::::ooooo:::::otttttt:::::::tttttt    
    SSS::::::::SS   h::::::h   h::::::ho::::o     o::::o      t:::::t          
       SSSSSS::::S  h:::::h     h:::::ho::::o     o::::o      t:::::t          
            S:::::S h:::::h     h:::::ho::::o     o::::o      t:::::t          
            S:::::S h:::::h     h:::::ho::::o     o::::o      t:::::t    tttttt
SSSSSSS     S:::::S h:::::h     h:::::ho:::::ooooo:::::o      t::::::tttt:::::t
S::::::SSSSSS:::::S h:::::h     h:::::ho:::::::::::::::o      tt::::::::::::::t
S:::::::::::::::SS  h:::::h     h:::::h oo:::::::::::oo         tt:::::::::::tt
 SSSSSSSSSSSSSSS    hhhhhhh     hhhhhhh   ooooooooooo             ttttttttttt  
                                                                           
   SSSSSSSSSSSSSSS      tttt                                               
 SS:::::::::::::::S  ttt:::t                                               
S:::::SSSSSS::::::S  t:::::t                                               
S:::::S     SSSSSSS  t:::::t                                               
S:::::S        ttttttt:::::ttttttt      aaaaaaaaaaaaa  rrrrr   rrrrrrrrr       ssssssssss
S:::::S        t:::::::::::::::::t      a::::::::::::a r::::rrr:::::::::r    ss::::::::::s
 S::::SSSS     t:::::::::::::::::t      aaaaaaaaa:::::ar:::::::::::::::::r ss:::::::::::::s
  SS::::::SSSSStttttt:::::::tttttt               a::::arr::::::rrrrr::::::rs::::::ssss:::::s
    SSS::::::::SS    t:::::t              aaaaaaa:::::a r:::::r     r:::::r s:::::s  ssssss
       SSSSSS::::S   t:::::t            aa::::::::::::a r:::::r     rrrrrrr   s::::::s
            S:::::S  t:::::t           a::::aaaa::::::a r:::::r                  s::::::s
            S:::::S  t:::::t    tttttta::::a    a:::::a r:::::r            ssssss   s:::::s
SSSSSSS     S:::::S  t::::::tttt:::::ta::::a    a:::::a r:::::r            s:::::ssss::::::s
S::::::SSSSSS:::::S  tt::::::::::::::ta:::::aaaa::::::a r:::::r            s::::::::::::::s
S:::::::::::::::SS     tt:::::::::::tt a::::::::::aa:::ar:::::r             s:::::::::::ss
 SSSSSSSSSSSSSSS         ttttttttttt    aaaaaaaaaa  aaaarrrrrrr              sssssssssss"""
else:
    banner = r"""
 ____  _           _     ____  _
/ ___|| |__   ___ | |_  / ___|| |_ __ _ _ __ ___
\___ \| '_ \ / _ \| __| \___ \| __/ _` | '__/ __|
 ___) | | | | (_) | |_   ___) | || (_| | |  \__ \
|____/|_| |_|\___/ \__| |____/ \__\__,_|_|  |___/"""


# Функции...
def main_cli():
    try:
        if Windows:
            subprocess.call(['chcp', '65001'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    except Exception:
        pass

    global url_repo, repo, repo_api, path
    try:
        screen_banner()
        console.print("Enter [bold green]url[/bold green] (Repository On GitHub) or '[bold green]history[/bold green]': ",
                      highlight=False, end="")
        url_repo = input("")
    except KeyboardInterrupt:
        try:
            name_os = f"{os.getlogin()}, "
        except Exception:
            name_os = ""
        console.print(f"\n[bold red][italic]Interrupt, {name_os}please think about how open source projects exist.[/italic][/bold red]")
        win_exit()
    repo = url_repo.rsplit(sep='/', maxsplit=1)[-1]
    repo_api = '/'.join(url_repo.rsplit(sep='/', maxsplit=2)[-2:])
    path = path_repo()

    try:
        if "shotstars" in url_repo.lower(): 
            with console.status("[bold blue] 💡 An Easter egg has been discovered...", spinner='noise'):
                try:
                    r_east = requests.get(url="https://pepy.tech/projects/shotstars?timeRange=threeMonths&category=version" + \
                                              "&includeCIDownloads=true&granularity=daily&viewType=line", 
                                          headers = {'User-Agent': f'Mozilla/5.0 (X11; Linux x86_64; rv:' + \
                                                     f'{random.randint(119, 127)}.0) Gecko/20100101 Firefox/121.0'}, timeout=7)

                    r_east_ = re.search(r'totalDownloads\\":(\d+)', r_east.text)
                    if r_east_:
                        print('')
                        console.print(Panel.fit(f"[bold white on blue]{r_east_.group(1)}[/bold white on blue]",
                                                title='total ShotStars software downloads',
                                                border_style="bold blue"),
                                      justify="center")
                        print('')
                except Exception as e:
                    console.print(f"[bold red][!] Network connection failure (Internet Censorship?),\n" + \
                                  f"    unable to receive data.\n\nexit.[/bold red]")
            win_exit()
        if url_repo.lower() == "history" or url_repo.lower() == "his":
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
            if os.path.isfile(f"{path.replace(repo, '')}/stars.jpg") is False:
                shutil.copy(image, f"{path.replace(repo, '')}/stars.jpg")
                if Linux: # снятие исполняемого бита для shotstars_cli.bin build версии.
                    os.chmod(f"{path.replace(repo, '')}/stars.jpg", 0o644)
            his()
            check_token()
            parsing(diff=True)
        else:
            console.print(f"\n[bold green]A new repository has been added to the tracking " + \
                          f"database: '[/bold green][cyan]{repo}[/cyan][bold green]'.\nOn subsequent/re-scanning of the " + \
                          f"repository, ShotStars will attempt to calculate stars.[/bold green]", highlight=False)
            his()
            check_token()
            parsing()
    except KeyboardInterrupt:
        console.print(f"\n[bold red][italic]Interrupt[/italic][/bold red]")
        os.kill(os.getpid(), signal.SIGBREAK if Windows else signal.SIGKILL)


def screen_banner():
    "Заставка/баннер."
    path_ = os.path.join(os.environ["LOCALAPPDATA" if Windows else "HOME"], 'ShotStars' if Windows else '.ShotStars', 'results')

    if os.path.exists(path_):
        lst_dir = [d for d in os.scandir(path_) if d.is_dir()]

        if len(lst_dir) > 3 and (not Windows or (Windows and int(platform.version().split('.')[2]) >= 19045)):
            with console.screen(style="dim cyan") as screen:
                for count in range(5, 0, -1):
                    text_screen = Align.center(Text.from_markup(f"SHOTSTARS OVER FAB TOOL TO TRACK STARS!\n\n{count}",
                                                                justify="center"))
                    if count < 5:
                        text_screen = Align.center(Text.from_markup(f"support with a donation or a star\n\n{count}",
                                                                    justify="center"))
                    if count < 2:
                        text_screen = Align.center(Text.from_markup(f"[blink]support with a donation or a star[/blink]\n\n{count}",
                                                                    justify="center"))

                    screen.update(Panel(text_screen))
                    time.sleep(1)

    console.print(f"[yellow]{banner}[/yellow]\n{__version__}, author: https://github.com/snooppr\n")


def cross_user_detect(base_users):
    """
    Последовательно читаем файлы с указанным именем из ВСЕХ подкаталогов,
    находим минимум 2-х перекрестных user-ов, встречающихся более чем в одном файле.
    """
    cross_user = defaultdict(set)
    base_dir = os.path.join(os.path.dirname(path))

    for dir_ in os.scandir(base_dir):
        if dir_.is_dir():
            subfile_path = os.path.join(dir_.path, "new.txt")
            if os.path.isfile(subfile_path):
                with open(subfile_path, 'r', encoding='utf-8') as f:
                    git_users = set(f.read().splitlines())
                    for user in base_users:
                        if user in git_users:
                            cross_user[user].add(dir_.name)

    common_users = {} # Фильтруем user/repo до 2-х и боле резуьтатов (ключи: user, значения: кортежи-repo).
    common_repo = set()
    for k, v in cross_user.items():
        if len(v) > 1:
            common_repo.update(v)
            common_users[k] = tuple(sorted(list(v)))

    common_repo.discard(repo)

    if common_users:
        console.rule(f"[bold blue]cross-users ({len(common_users)}), regarding the repository ({repo})[/bold blue]", characters="#")
        print("")
        console.print(Panel.fit(f"[yellow]([/yellow]{repo}[yellow])[/yellow] VS [yellow]([/yellow]{', '.join(common_repo)}[yellow])[/yellow]",
                                title=f"cross-users found in repositories (1 VS {len(common_repo)})",
                                border_style="magenta"))

        padding = 0 if Android else (0, 1)
        table_his = Table(title=f"\n[bold red]CROSS-USERS (in CLI = max 5 users, in HTML = full users)[/bold red]",
                          title_justify="center", header_style='bold red', style="bold red", padding=padding, show_lines=True)
        table_his.add_column("N", justify="left", style="bold green", no_wrap=False)
        table_his.add_column("Q/S", justify="left", style="red", no_wrap=False)
        table_his.add_column("GitHub username", justify="left", style="bold blue", overflow="fold", no_wrap=False)
        table_his.add_column("GitHub repositories", justify="left", style="bold yellow", overflow="fold", no_wrap=False)

        sorted_items = sorted(common_users.items(), key=lambda item: (-len(item[1]), item[0]))
        for N, (username, repository) in enumerate(sorted_items[:5], 1):
            table_his.add_row(str(N), str(len(repository)), f'https://github.com/{username}', ", ".join(repository))
        console.print(table_his)

        with open(os.path.join(os.path.dirname(path), "dynamic_crossusers.txt"), "w", encoding="utf-8") as f:
            f.write(f"<dynamically updated file>\n\n")
            f.write(f"CROSS-USERS [regarding the repository: {repo}]:: {len(common_users)} users\n")
            f.write(f"CROSS-USERS [found in repositories: 1 VS {len(common_repo)}]:: ({repo}) VS ({', '.join(common_repo)}) repositories\n\n")
            for username, repository in sorted_items:
                print(f"https://github.com/{username} ({len(repository)}):\n  ", '\n   '.join(repository), '\n', file=f)


def agregated_date(filename):
    """
    Читаем HTML-файл, извлекаем и агрегируем данные: дата и кол-во users (для расчета 'gone stars').
    Либо возвращаем реальный парсинг по github-api (new stars).
    """
    if isinstance(filename, list):
        return filename

    aggregated_data = defaultdict(int)
    pattern = re.compile(r"<span class='color2'>\d{4}-\d{2}-\d{2}_\d{2}:\d{2}\s*—\s*(\d{4}-\d{2}-\d{2})_\d{2}:\d{2}</span>.*?" + \
                         r"users__<b>(\d+)</b>", re.IGNORECASE)

    if not os.path.exists(filename):
        return aggregated_data

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            fr = f.read().splitlines()
            for i in fr:
                match = pattern.search(i)
                if match:
                    date_str_original = match.group(1)
                    user_count_str = match.group(2)
                    aggregated_data[date_str_original] += int(user_count_str)
    except Exception as e:
        console.print(f"[bold red]Error data in HTML | {e}[/bold red]\n")
        aggregated_data.clear()

    return aggregated_data


def calc_stars(aggregated_data):
    """Получаем дату, и на неё кол-во звезд"""
    sorted_items = sorted(aggregated_data.items(), key=lambda item: datetime.datetime.strptime(item[0], '%Y-%m-%d'))
    dates_for_plot = [item[0] for item in sorted_items]
    counts_for_plot = [item[1] for item in sorted_items]

    return dates_for_plot, counts_for_plot


def generate_plots(aggregated_data, source_filename, months_stars, years_stars, hours_stars, mean_year, mean_days, dif_date):
    """Генерация CLI и HTML графиков"""
    if not aggregated_data:
        return None
    elif isinstance(aggregated_data, list):
        aggregated_data1, aggregated_data2 = aggregated_data
        dates_for_plot, counts_for_plot = calc_stars(aggregated_data1)
        dates_for_plot2, counts_for_plot2 = calc_stars(aggregated_data2)
    else:
        dates_for_plot, counts_for_plot = calc_stars(aggregated_data)

    base_filename = os.path.basename(source_filename)

# График для CLI.
    if Windows:
        if base_filename == 'all_new_stars.html':
            console.print(f"\n[yellow][!] The graph in CLI is built only for OS: GNU/Linux; macOS and Android/Termux.\n" + \
                          f"    See graph in HTML report.[/yellow]\n")
    else:
        try:
            plt_cli.clear_figure()
            plotext_date_format = 'Y-m-d'
            plt_cli.date_form(plotext_date_format)
            plt_cli.xlabel("Date")
            plt_cli.ylabel("Q Users")
            plt_cli.grid(True, True)
            plt_cli.ticks_color('yellow')

            if base_filename == 'all_new_stars.html':
                plt_cli.title(f"NEW_STARS, '{repo}' (real parsing)")
                plt_cli.canvas_color('black')
                plt_cli.axes_color('green')
            elif base_filename == 'all_gone_stars.html':
                plt_cli.title(f"GONE_STARS, '{repo}' (calculations)")
                plt_cli.canvas_color('black')
                plt_cli.axes_color('red')

            plt_cli.xticks(dates_for_plot)
            plt_cli.yticks(range(0, max(counts_for_plot) + 1))

            for i in range(len(dates_for_plot)):
                plt_cli.plot([dates_for_plot[i], dates_for_plot[i]], [0, counts_for_plot[i]], marker='*', color='blue+')

            plt_cli.show()

            print("\n")
        except Exception:
            console.print(f"[bold red]CLI Graph for {source_filename} — not created[/bold red]")

# Графики для HTML.
    try:
# Преобразовываем дату str > datetime для реального отображения масштаба на графике.
        fig = plt_html.Figure()
        plot_bgcolor = '#f0f0f0'
        paper_bgcolor = '#e0e0e0'

        if base_filename == 'all_new_stars.html':
            line_color = 'lime'
            marker_color = 'green'
        elif base_filename == 'all_gone_stars.html':
            line_color = 'red'
            marker_color = '#a73c3c'
# строим 1-й в HTML-график.
        fig.add_trace(plt_html.Scatter(x=dates_for_plot, y=counts_for_plot, mode='markers',
                      marker=dict(color=marker_color, size=8, symbol='star'),
                      error_y=dict(type='data', arrayminus=counts_for_plot, array=[0] * len(counts_for_plot),
                                   visible=True, thickness=1, width=0, color=line_color), name='all stars',
                      customdata=counts_for_plot, hovertemplate=("Date: %{x}<br>Stars: %{customdata}<extra></extra>")))

        fig.add_trace(plt_html.Scatter(x=dates_for_plot, y=[mean_days] * len(dates_for_plot), mode='lines',
                                       name=f'mean = {round(mean_days, 1)} stars / days', opacity=0.70,
                                       line=dict(color='red', width=2)))

        fig.update_layout(title=f"Graph N1. Dynamics userstars, repository '<b>{repo}</b>' " + \
                                f"␥ Created with <a href='https://github.com/snooppr/shotstars'>Shotstars software</a>.",
                          xaxis_title="Date", yaxis_title="Quantity stars",
                          xaxis=dict(tickformat='%Y-%m-%d', showgrid=True, gridwidth=1, gridcolor='lightgray'),
                          yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
                          plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor)

        if not isinstance(aggregated_data, list):
            fig.write_html(f"{path}/graph_{base_filename}")
        else: # строим множество HTML-графиков.
            fig2 = plt_html.Figure()

            fig2.add_trace(plt_html.Scatter(x=dates_for_plot2, y=counts_for_plot2, mode='lines+markers',
                                            marker=dict(size=3, symbol='star'), line=dict(shape='spline', width=5)))

            fig2.update_layout(title=f"Graph N2. Cumulative growth of stars, repository '<b>{repo}</b>' " + \
                                     f"␥ Created with <a href='https://github.com/snooppr/shotstars'>Shotstars software</a>.",
                               xaxis_title='Date', yaxis_title='Quantity stars',
                               xaxis=dict(tickformat='%Y-%m-%d'), autosize=True,
                               yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
                               plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                               width=None, height=None)

            x, y = map(list, zip(*months_stars))
            fig3 = plt_html.Figure([plt_html.Bar(y=y, x=x, name='Month', opacity=0.90,
                                    marker=dict(color='orange', line=dict(color='black', width=2)))])

            fig3.update_layout(title=f"Histogram N1. Cumulative set of stars by <b>month</b>, repository '<b>{repo}</b>' " + \
                                     f"␥ Created with <a href='https://github.com/snooppr/shotstars'>Shotstars software</a>.",
                               xaxis_title="Month", yaxis_title="Quantity stars",
                               plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor)

            x, y = map(list, zip(*years_stars))
            fig4 = plt_html.Figure([plt_html.Bar(y=y, x=x, name='Year',
                                   marker=dict(color='orange', line=dict(color='grey', width=4)))])

            if dif_date > 365:
                fig4.add_trace(plt_html.Scatter(x=x, y=[mean_year] * len(x), mode='lines',
                               name=f'mean = {round(mean_year, 1)} stars / year',
                               line=dict(color='red', width=3)))

            fig4.update_layout(title=f"Histogram N2. Cumulative set of stars by <b>year</b>, repository '<b>{repo}</b>' " + \
                                     f"␥ Created with <a href='https://github.com/snooppr/shotstars'>Shotstars software</a>.",
                               xaxis_title="Year", yaxis_title="Quantity stars", xaxis=dict(dtick=1, tickmode='linear'),
                               barmode='overlay', plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor)


            x, y = map(list, zip(*hours_stars))
            fig5 = plt_html.Figure([plt_html.Bar(y=x, x=y, name='Hours', orientation='h',
                                    hovertemplate=("Hours: %{y}<br>Stars: %{x}<extra></extra>"),
                                    marker=dict(color='blue'))])

            fig5.update_layout(title=f"Histogram N3. Star Hour (distribution of stars by <b>hour, {local_tzone} time zones</b>), " + \
                                     f"repository '<b>{repo}</b>' " + \
                                     f"␥ Created with <a href='https://github.com/snooppr/shotstars'>Shotstars software</a>.",
                               xaxis_title="Quantity stars", yaxis_title="Hours", yaxis=dict(dtick=1, tickmode='linear'),
                               xaxis=dict(gridcolor='lightgray'),
                               plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor)


            plot_html = fig.to_html(full_html=False, include_plotlyjs=False)
            plot_html2 = fig2.to_html(full_html=False, include_plotlyjs=False)
            plot_html3 = fig3.to_html(full_html=False, include_plotlyjs=False)
            plot_html4 = fig4.to_html(full_html=False, include_plotlyjs=False)
            plot_html5 = fig5.to_html(full_html=False, include_plotlyjs=False)

            with open(f"{path}/graph_{base_filename}", 'w', encoding='utf-8') as f:
                f.write(f"""
<html>
<head>
    <meta charset="utf-8" />
    <script type="text/javascript">window.PlotlyConfig = {{MathJaxConfig: 'local'}};</script>
    <script type="text/javascript">{get_plotlyjs()}</script>
    <title>📈 Shotstars, add_stars</title>
    <style>
        body {{
            margin: 0;
            padding: 15px;
            box-sizing: border-box;
        }}
        .plot-container {{
            width: 100%;
            margin-bottom: 30px;
            box-sizing: border-box;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="plot-container">
        {plot_html}
    </div>

    <div class="plot-container">
        {plot_html2}
    </div>

    <div class="plot-container">
        {plot_html3}
    </div>

    <div class="plot-container">
        {plot_html4}
    </div>

    <div class="plot-container">
        {plot_html5}
    </div>
</body>
</html>""")
    except Exception as e:
         console.print(f"[bold red]HTML Graph for graph_{base_filename} — not created | {e}[/bold red]")


def backup_table():
    "Бэкап истории таблицы сканирований, в случае перехода на обновленную версию Shotstars v2.0+."
    info = os.path.join(os.path.dirname(path), "backup_history.txt")

    console.print(f"\nShotstars [cyan]v2.0[/cyan] has an updated format for the '[cyan]scan table history[/cyan]': " + \
                  f"a '[cyan]stars[/cyan]' column has been added. [bold red]table history will be cleared[/bold red], " + \
                  f"but a backup will be made. You can find the history backup here:\n'" + \
                  f"[cyan]{info}[/cyan]'.", highlight=False)

    with open(os.path.join(os.path.dirname(path), "history.json"), "r") as history_urls:
        file = json.load(history_urls)
        url_table_lst = [f"https://github.com/{k}" for k in file]
    with open(info, "w", encoding="utf-8") as backup_history_url:
        backup_history_url.write("Saved urls (backup) that were previously in the Shotstars history table.\n\n")
        backup_history_url.write('\n'.join(url_table_lst))

    os.remove(os.path.join(os.path.dirname(path), "history.json"))
    os.execl(sys.executable, sys.executable, *sys.argv)


def his(check_file=False, history=False):
    """История сканирований."""
    if not os.path.isfile(os.path.join(os.path.dirname(path), "history.json")):
        with open(os.path.join(os.path.dirname(path), "history.json"), 'w') as not_his_w:
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
        with open(os.path.join(os.path.dirname(path), "history.json"), 'r') as his_file:
            his_dict = json.load(his_file)

            dict_urls = {}
            for num, (url, his_date) in enumerate(his_dict.items(), 1):
                try: #In Shotstars version 2.0 the table format has been changed.
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
    """
    Создание каталога для данных репозиториев.
    v4.5 Переименование каталога в скрытый на GNU/Linux из 'ShotStars/.ShotStars'.
    """
    try:
        if not Windows:
            replace_shotstars_dir = os.path.join(os.environ["HOME"], 'ShotStars')
            if os.path.exists(replace_shotstars_dir):
                shutil.move(replace_shotstars_dir, os.path.join(os.environ["HOME"], '.ShotStars'))
    except Exception:
        pass

    path = os.path.join(os.environ["LOCALAPPDATA" if Windows else "HOME"], 'ShotStars' if Windows else '.ShotStars', 'results', repo)
    os.makedirs(path, exist_ok=True)

    return path


def check_token():
    """Github-token проверка."""
    if not os.path.isfile(os.path.join(os.path.dirname(path), "config.ini")):
        config.add_section('Shotstars')
        config.set('Shotstars', 'token', 'None')
        with open(os.path.join(os.path.dirname(path), "config.ini"), 'w') as config_file:
            config.write(config_file)


def win_exit():
    """
    Удержание окна консоли скомпилированной версии 'shotstars_cli.exe' для OS Windows.
    Сначала цветной 'print', потом чистый 'input', иначе прогресс в некоторых случаях может перекрывать сообщение.
    """
    if Windows:
        console.print("\npress key <ENTER> --> exit")
        input("")

    sys.exit()


def dif_time():
    """
    Диапазон прошедшего времени: от последнего сканирования к текущему сканированию.
    Замена устаревшей функции в Python3.12+: "utcfromtimestamp".
    """
    delta = datetime.datetime.today() - datetime.datetime.fromtimestamp(date_file_new)
    return f"{delta.days}d. {(datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc) + delta).strftime('%Hh. %Mm.')}"


def finish(token, stars=None, report=None):
    """Финишное время, проверка наличие/отсутствие токена и заполнение истории сканирований."""
    print('\nFinish', round(time.perf_counter() - time_start, 1), f"sec, in {timeout()}.")

    if not report:
        print("Report.html not created, no movement of stars.")

    if token == "None":
        print("GitHub token not provided.")
    elif token != "None":
        print("GitHub-token is used!")

    with open(os.path.join(os.path.dirname(path), "history.json"), "r") as his_r:
        his_file = json.load(his_r)
        try:
            his_file.update({repo_api: [int(time.time()), stars]})
            his_file = dict(sorted(his_file.items(), key=lambda x: x[1][0], reverse=True))
        except Exception:
            his_r.close()
            backup_table()
    with open(os.path.join(os.path.dirname(path), "history.json"), "w") as his_w:
        json.dump(his_file, his_w, indent=1)


def limited(req, token):
    """Расчет времени снятия лимита Github-API."""
    headers_time = int(req.headers.get('X-RateLimit-Reset')) + 60
    minut = datetime.datetime.fromtimestamp(headers_time) - datetime.datetime.today()
    minut = int(minut.seconds / 60)
    console.print("\n[bold red]Attention! The API limit has probably been exceeded, the block will presumably be lifted:",
                  time.strftime('%Y-%m-%d_%H:%M', time.localtime(headers_time)), f"::: ({minut} min.)")
    if token == "None":
        console.print(Panel.fit("Limitations: ~limit max '30 requests/hour' or '6000 stars/hour'", title="GitHub API/No Token"))
        console.print("\n[bold yellow][!] Shotstars does not process repositories with stars > 6K+ without a github token " + \
                      "by default.\nUsing a free GitHub token, the limits are significantly increased\n(500K+ stars/hour or " + \
                      "max scanned repository with 40K stars). " + \
                      "\n\nView Readme: https://github.com/snooppr/shotstars#%EF%B8%8F-github-restrictions[/bold yellow]")
    else:
        console.print(Panel.fit("Limitations: ~limit max '500K stars/hour'", title="GitHub API/Token Used"))

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


def quartiles(cnt_sum, none_statistic=None, dif_date=None, months=None, month=False, year=False):
    """Расчет звезд и процентного соотношения месяца/года, квартили (x < Q1; x in Q1-Q3; x > Q3)."""
    if (month and dif_date > 32) or (year and dif_date > 365):
        l_cnt_sum = list(sorted(cnt_sum.values()))
        Q1 = statistics.median(l_cnt_sum[:len(l_cnt_sum) // 2])
        Q3 = statistics.median(l_cnt_sum[(len(l_cnt_sum) + 1) // 2:])
        Q1_Q3_index = len([x for x in l_cnt_sum if Q1 <= x <= Q3 and x != 0])
        Q3_index = len([x for x in l_cnt_sum if x > Q3 and x != 0])
        sum_v = sum(cnt_sum.values())
        if month:
            Q3_print = [f"{str(months[i[0]-1]).upper()}: {i[1]}_STARS___({round(i[1]*100/sum_v, 1)}%)"
                        for i in cnt_sum.most_common(Q3_index)]
            Q1_Q3_print = [f"{months[i[0]-1]}: {i[1]}_Stars___({round(i[1]*100/sum_v, 1)}%)"
                           for i in cnt_sum.most_common()[Q3_index:Q3_index+Q1_Q3_index]]
            Q1_print = [f"{str(months[i[0]-1]).lower()}: {i[1]}_stars___({round(i[1]*100/sum_v, 1)}%)"
                        for i in cnt_sum.most_common()[Q3_index+Q1_Q3_index:]]
        if year:
            Q3_print = [f"{i[0]}: {i[1]}_STARS___({round(i[1]*100/sum_v, 1)}%)"
                        for i in cnt_sum.most_common(Q3_index)]
            Q1_Q3_print = [f"{i[0]}: {i[1]}_Stars___({round(i[1]*100/sum_v, 1)}%)"
                           for i in cnt_sum.most_common()[Q3_index:Q3_index+Q1_Q3_index]]
            Q1_print = [f"{i[0]}: {i[1]}_stars___({round(i[1]*100/sum_v, 1)}%)"
                        for i in cnt_sum.most_common()[Q3_index+Q1_Q3_index:]]
        return Q1_print, Q1_Q3_print, Q3_print
    else:
        return [none_statistic], [none_statistic], [none_statistic]

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

    config.read(os.path.join(os.path.dirname(path), "config.ini"))
    token = config.get('Shotstars', 'token')
    if token != "None":
        head = {'User-Agent': f'Shotstars {__version__}', 'Authorization': f'Bearer {token}'}
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
        if token != "None":
            console.print(f"\n[bold red]Your GitHub token may have expired (default: token = None), check:\n" + \
                          f"{os.path.join(os.path.dirname(path), 'config.ini')}[/bold red]")
        if not os.path.isfile(f"{path}/new.txt"):
            shutil.rmtree(path, ignore_errors=True)
        win_exit()
    except Exception:
        limited(req, token)

# Вывод на печать кол-ва звезд, дату создания проекта и описание (если присутствует).
    try:
        size_repo = "N/O" if r.get('size') is None else round(r.get('size') / 1024, 2)
        created_at = -1 if r.get('created_at') is None else r.get('created_at').split("T")[0]
        created_at_days = (datetime.datetime.today() - datetime.datetime.strptime(created_at, '%Y-%m-%d')).days if created_at != -1 else -1
        push = "N/O" if r.get('pushed_at') is None else r.get('pushed_at')
        try:
            push_ = datetime.datetime.strptime(push, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
            push_ = push_.astimezone().strftime('%Y-%m-%d__%H:%M') + f"_{local_tzone}"
        except Exception:
            push_ = "BAD!"
        title_repo = "No repository description available" if r.get('description') is None else r.get('description')
        console.print(f"\n[cyan]Size::[/cyan] ~{size_repo} MB" + \
                      f"\n[cyan]GitHub-rating::[/cyan] {stars} stars" + \
                      f"\n[cyan]Date-of-creation::[/cyan] {created_at} ({created_at_days} days)" + \
                      f"\n[cyan]Date-update (including hidden update)::[/cyan] {push_}" + \
                      f"\n[cyan]Repository-description::[/cyan] {title_repo}", highlight=False)
    except Exception:
        console.print('[red]Check GitHub api (buggy).\nReport issue to developer: "https://github.com/snooppr/shotstars/issues"')
        win_exit()

    if token == "None" and pages > 60:
        console.print("\n[bold yellow][!] Shotstars does not process repositories with stars > 6K+ without a github token " + \
                      "by default.\nUsing a free GitHub token, the limits are significantly increased\n(500K+ stars/hour or " + \
                      "max scanned repository with 40K stars). " + \
                      "\n\nView Readme: https://github.com/snooppr/shotstars#%EF%B8%8F-github-restrictions[/bold yellow]")
        shutil.rmtree(path, ignore_errors=True)
        win_exit()
    elif token != "None" and pages > 400:
        console.print("\n[bold yellow][!] Using a github token, the maximum crawlable repository on Shotstars " + \
                      "is limited to 40K stars.[/bold yellow]")
        shutil.rmtree(path, ignore_errors=True)
        win_exit()

# Обход и сохранение всех user's, которые ставили/снимали звезды репозиторию.
    if Android:
        thread_max = pages if pages <= os.cpu_count() * 2 else 14
    else:
        thread_max = pages if pages <= 18 else 18
    executor = ThreadPoolExecutor(max_workers=thread_max)

    spinner = 'earth' if diff else 'material'
    lst_new, lst_star_hours, futures, datestars_user = [], [], {}, defaultdict(set)
    with console.status("[cyan]Working", spinner=spinner):
        for page in range(1, pages+1):
            futures[executor.submit(my_session.get, headers={**head, 'Accept': 'application/vnd.github.star+json'}, timeout=6,
                                    url=f'https://api.github.com/repos/{repo_api}/stargazers?per_page=100&page={page}')] = None
        try:
            for future in as_completed(futures):
                data = future.result(timeout=12)

                for num in data.json():
                    git_username = num.get("user").get("login")
                    lst_new.append(git_username)
                    datestars_user[num.get("starred_at").split("T")[0]].add(git_username)

                    time_h = datetime.datetime.strptime(num.get("starred_at"), '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
                    lst_star_hours.append(time_h.astimezone().hour)

                futures.pop(future, None)
        except Exception:
            limited(req, token)

        try:
            executor.shutdown()
        except Exception:
            pass

# Сохранение даты и всех пользователей, добавивших звезды, в json.
    json_date_users = {f"{d_}  ({len(u_)} stars)": [f"https://github.com/{_}" for _ in u_]
                       for d_, u_ in sorted(datestars_user.items())}
    with open(f"{path}/date_users.json", 'w', encoding='utf-8') as save_datestars_user:
        json.dump(json_date_users, save_datestars_user, ensure_ascii=False, indent=2)

# Статистика.
    start_date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
    end_date = datetime.datetime.today()
    Maximum_stars_in_date = Counter({date: len(users) for date, users in datestars_user.items()}) #data для 1-го гр. add_stars.
    dif_date = (end_date - start_date).days

    cumulative_datestars = Counter() #data для 2-го гр. add_stars.
    s_total = 0
    for k, v in sorted(Maximum_stars_in_date.items()):
        s_total += v
        cumulative_datestars[k] = s_total

    _Maximum_stars_in_date = Maximum_stars_in_date.copy()
    while start_date <= end_date:
        date_str = start_date.strftime('%Y-%m-%d')
        _Maximum_stars_in_date.setdefault(date_str, 0)
        start_date += datetime.timedelta(days=1)

    hours_stars = Counter(lst_star_hours)
    [hours_stars.setdefault(i, 0) for i in range(24)]
    hours_stars = sorted(hours_stars.items())

    sort_alldate_stars = sorted(_Maximum_stars_in_date.items(), key=lambda item: datetime.datetime.strptime(item[0], '%Y-%m-%d'))

    if dif_date > 31:
        trend = statistics.median([i[1] for i in sort_alldate_stars[-30:]])
    else:
        trend = statistics.median([i[1] for i in sort_alldate_stars])

    trend = f"1 stars / day" if trend == 0.5 else f"{round(trend)} stars / day"

    mean_year = statistics.mean([i[1] for i in sort_alldate_stars]) * 365 if dif_date > 365 else -1
    mean_days = statistics.mean([i[1] for i in sort_alldate_stars])

    none_statistic = "The repository is still young, not enough data"
    if dif_date > 62:
        relative_start = statistics.median([i[1] for i in sort_alldate_stars[-60:-30]])
        relative_end = statistics.median([i[1] for i in sort_alldate_stars[-30:]])
        try: #медиана в процентах.
            relative_percentage = f"{round(((relative_end - relative_start) / relative_start) * 100, 2)} %"
        except ZeroDivisionError:
            relative_percentage = "—"

        relative_start_ = statistics.mean([i[1] for i in sort_alldate_stars[-60:-30]])
        relative_end_ = statistics.mean([i[1] for i in sort_alldate_stars[-30:]])
        sum_start = sum([i[1] for i in sort_alldate_stars[-60:-30]])
        sum_end = sum([i[1] for i in sort_alldate_stars[-30:]])
        average_change_stars = f"{sum_end - sum_start} stars"
        try: #среднее в разах.
            if (relative_end_ / relative_start_) < 1:
                average_change = f"-{relative_start_ / relative_end_:.2f} times"
            else:
                average_change = f"{relative_end_ / relative_start_:.2f} times"
        except ZeroDivisionError:
            average_change = "—"

        stdev = statistics.stdev([i[1] for i in sort_alldate_stars])
        if stdev < 4: marketing, marketing_color, fuckstars = "—", "—", "—"
        elif 4 < stdev < 6: marketing, marketing_color, fuckstars = "Low", "[green]Low[/green]", "—"
        elif 6 < stdev < 11: marketing, marketing_color, fuckstars = "Medium", "[yellow]Medium[/yellow]", "—"
        elif 11 < stdev < 17: marketing, marketing_color, fuckstars = "High", "[red]High[/red]", "—"
        elif 17 < stdev < 35: marketing, marketing_color, fuckstars = "Hard", "[black on red]Hard[/black on red]", "Yes"
        elif stdev > 35:
            marketing, marketing_color = "Hard+", "[black on red]Hard+[/black on red]"
            fuckstars = "Yes, multiple attempts to promote fake stars"
    else:
        relative_percentage = none_statistic
        average_change = none_statistic
        average_change_stars = none_statistic
        marketing = none_statistic
        marketing_color = none_statistic
        fuckstars = none_statistic

## Расчет месяцев с самым высоким и низким трафиком по звездам / Расчет по годам.
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_sum = defaultdict(int)
    years_sum = defaultdict(int)
    for date_str, _star in sort_alldate_stars:
        dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        month_number = dt.month
        year_number = dt.year
        month_sum[month_number] += _star
        years_sum[year_number] += _star

    cnt_month_sum = Counter(month_sum)
    cnt_year_sum = Counter(years_sum)
    high_stars_month = months[cnt_month_sum.most_common()[0][0] - 1]
    low_stars_month = months[cnt_month_sum.most_common()[-1][0] - 1]

# Data для 3-го графика.
    months_stars = [(months[m_-1], s_) for m_, s_ in sorted(month_sum.items(), key=lambda item: item[0])]
    years_stars = [(y_, s_) for y_, s_ in sorted(years_sum.items(), key=lambda item: item[0])]

## Расчет месяцев/лет по квартилям: x < Q1; x в Q1-Q3; x > Q3.
    Q1_print_m, Q1_Q3_print_m, Q3_print_m = quartiles(cnt_month_sum, none_statistic=none_statistic,
                                                      dif_date=dif_date, months=months, month=True)
    Q1_print_y, Q1_Q3_print_y, Q3_print_y = quartiles(cnt_year_sum, none_statistic=none_statistic,
                                                      dif_date=dif_date, year=True)

    max_stars, in_date = Maximum_stars_in_date.most_common(1)[0][-1], Maximum_stars_in_date.most_common(1)[0][0]

## Private stars
    private_stars = abs(stars - sum(cnt_month_sum.values()))

## Самый продолжительный период без прибавления звезд.
    max_zeros, current_zeros = 0, 0
    start_date, max_start_date = None, None
    for date__, stars__ in sort_alldate_stars:
        if stars__ == 0:
            if current_zeros == 0:
                start_date = date__
            current_zeros += 1
        else:
            if current_zeros > max_zeros:
                max_zeros = current_zeros
                max_start_date = start_date
            current_zeros = 0

    if current_zeros > max_zeros:
        max_zeros = current_zeros
        max_start_date = start_date

    tuple_date_no_stars = (max_start_date, max_zeros) if max_start_date is not None else ("—", "—")
    try:
        end_date_no_stars = (datetime.datetime.strptime(tuple_date_no_stars[0], '%Y-%m-%d') + \
                             datetime.timedelta(days=tuple_date_no_stars[1])).strftime('%Y-%m-%d')
    except Exception:
        end_date_no_stars = "—"

## Печать инфострок.
    console.print(f"[cyan]Peak-stars-in-date::[/cyan] {max_stars} stars / {in_date}", highlight=False)
    console.print(f"[cyan]The-trend-of-adding-stars (forecasting)::[/cyan] {trend}", highlight=False)
    console.print(f"[cyan]Most-of-stars-month / Smallest-of-stars-month::[/cyan] " + \
                  f"{high_stars_month} / {low_stars_month}", highlight=False)

    if dif_date > 32:
        console.print(f"[cyan]Distribution-of-stars-by-month" + \
                      f"{' (' + str(private_stars) + ' private stars)' if private_stars != 0 else ''} " + \
                      f"({sum(cnt_month_sum.values())} stars)::[/cyan] {chr(10)}" + \
                      f"[bold green]{chr(10).join(Q3_print_m) if Q3_print_m else '-'*25}[/bold green]\n" + \
                      f"[bold yellow]{chr(10).join(Q1_Q3_print_m)}" + \
                      f"[/bold yellow]\n[bold red]{chr(10).join(Q1_print_m) if Q1_print_m else '-'*25}[/bold red]", highlight=False)

    if dif_date > 365:
        console.print(f"[cyan]Distribution-of-stars-by-year ({sum(cnt_month_sum.values())} stars)::[/cyan] {chr(10)}" + \
                      f"[green]{chr(10).join(Q3_print_y) if Q3_print_y else '-'*25}[/green]\n" + \
                      f"[yellow]{chr(10).join(Q1_Q3_print_y)}" + \
                      f"[/yellow]\n[red]{chr(10).join(Q1_print_y) if Q1_print_y else '-'*25}[/red]", highlight=False)

    console.print(f"[cyan]Longest-period-without-add-stars::[/cyan] " + \
                  f"{tuple_date_no_stars[0]} — {end_date_no_stars} ({tuple_date_no_stars[1]} days)", highlight=False)
    console.print(f"[cyan]Median-percentage-change (adding stars for the last month compared to the month before last" + \
                  f"::[/cyan] {relative_percentage}", highlight=False)
    console.print(f"[cyan]Average-change-in-fact (adding stars for the last month compared to the month before last)" + \
                  f"::[/cyan] {average_change} ({average_change_stars})", highlight=False)
    console.print(f"[cyan]Aggressive-marketing::[/cyan] {marketing_color}", highlight=False)
    console.print(f"[cyan]Fake-stars::[/cyan] {fuckstars}\n", highlight=False)

# Сравнение списков пользователей после временных сканирований для обнаружения в них изменений.
    with open(f"{path}/new.txt", "w", encoding="utf-8") as f_w:
        print(*lst_new, file=f_w, sep="\n")

    if diff:
        with open(f"{path}/old.txt", "r") as f_r:
            lst_old = f_r.read().split()

        diff_lst_dn = list(set(lst_old) - set(lst_new)) # убывание звезд.
        diff_lst_up = list(set(lst_new) - set(lst_old)) # прибавление звезд.

        if bool(diff_lst_dn) is False:
            console.print("[bold black on white]GONE stars not detected")
        if bool(diff_lst_up) is False:
            console.print("[bold black on white]NEW stars not detected")

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
        file_image = f"file://{os.path.join(path.replace(repo, ''), 'stars.jpg')}".replace('\\', '/')
        with open(f"{path}/report.html", "w", encoding="utf-8") as file_html:
            file_html.write("<!DOCTYPE html>\n<html lang='en'>\n\n<head>\n" + f"<title>💫({repo}) HTML-report</title>\n" + \
                            "<meta charset='utf-8'>\n<style>\n" + \
                            f"body {{background-image: url('{file_image}'); background-size: cover;\n" + \
"""background-repeat: no-repeat; background-attachment: fixed}
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
                            "title='open history adding stars'>open history</a>\n" + \
                            f"\n<a class='but' href='file://{path}/graph_all_new_stars.html' " + \
                            "title='open all history adding stars'>open graphs (5)</a>\n" + \
                            "</div>\n\n<div class='textcols-item'>\n<h4 style='color:#fc3f1d'>" + \
                            f"💫 Gone stars (-{per_stars_dn}%):</h4>\n")

            if bool(diff_lst_dn):
                table_dn = html_rec(file_html, diff_lst_dn, table_dn)

            sp = "<br>&nbsp;&nbsp;&nbsp;&nbsp;"
            n_graph = '1' if os.path.isfile(f"{path}/graph_all_gone_stars.html") else "0"
            file_html.write(f"\n<a class='but' href='file://{path}/all_gone_stars.html' " + \
                            "title='open history gone stars'>open history</a>\n" + \
                            f"\n<a class='but' href='file://{path}/graph_all_gone_stars.html' " + \
                            f"title='open history of calculations gone stars'>open graph ({n_graph})</a>\n" + \
                            "</div>\n</div>\n\n<br>\n<span class='donate' " + \
                            "style='color: white; text-shadow: 0px 0px 20px #333333'>" + \
                            f"<small><strong>\n💾 Size:: ~{size_repo} MB<br>\n" + \
                            f"✨ GitHub-rating:: {stars} stars<br>\n" + \
                            f"🌟 Peak-stars-in-date:: {max_stars} / {in_date}<br>\n" + \
                            f"📈 The-trend-of-adding-stars (forecasting):: {trend}<br>\n" + \
                            f"📅 Most-of-stars-month / Smallest-of-stars-month:: {high_stars_month} / {low_stars_month}<br>\n" + \
                            f"📅 Distribution-of-stars-by-month" + \
                            f"{' (' + str(private_stars) + ' private stars)' if private_stars != 0 else ''} " + \
                            f"({sum(cnt_month_sum.values())} stars):: {chr(10)}{sp}" + \
                            f"{sp.join(Q3_print_m) if Q3_print_m else '-'*25}\n{sp}{sp.join(Q1_Q3_print_m)}" + \
                            f"\n{sp}{sp.join(Q1_print_m) if Q1_print_m else '-'*25}<br>\n" + \
                            f"📅 Distribution-of-stars-by-year ({sum(cnt_month_sum.values())} stars):: {chr(10)}{sp}" + \
                            f"{sp.join(Q3_print_y) if Q3_print_y else '-'*25}\n{sp}{sp.join(Q1_Q3_print_y)}" + \
                            f"\n{sp}{sp.join(Q1_print_y) if Q1_print_y else '-'*25}<br>\n" + \
                            f"0️⃣ Longest-period-without-add-stars:: {tuple_date_no_stars[0]} — " + \
                            f"{end_date_no_stars} ({tuple_date_no_stars[1]} days)<br>\n" + \
                            f"📊 Median-percentage-change (adding stars for the last month compared " + \
                            f"to the month before last):: {relative_percentage}<br>\n" + \
                            f"📊 Average-change-in-fact (adding stars for the last month compared " + \
                            f"to the month before last):: {average_change} ({average_change_stars})<br>\n" + \
                            f"⏳ Date-of-creation:: {created_at} ({created_at_days} days)<br>\n" + \
                            f"⌛️ Date-update (including hidden update):: {push_}<br>\n" + \
                            f"📣 Aggressive-marketing:: {marketing}<br>\n" + \
                            f"🎃 Fake-stars:: {fuckstars}<br>\n" + \
                            f"📖 Repository-description:: {title_repo}</small></small></span><br>\n" + \
                            "<br>\n<span class='donate' style='color: white; text-shadow: 0px 0px 20px #333333'>" + \
                            "<small><small>╭📅 Changes over the past " + \
                            f"({dif_time()}): <br>├──{date}<br>└──{time.strftime('%Y-%m-%d_%H:%M', time.localtime())}" + \
                            "</strong></small></span>\n\n<div>\n<br>\n" + \
                            f"<a class='but' href='file://{path.replace(repo, '')}dynamic_crossusers.txt' " + \
                            "title='txt format'>open all cross-users</a>\n<br>\n" + \
                            f"<a class='but' href='file://{path}/date_users.json' " + \
                            "title='json format'>open date_all-stars_users</a>\n</div>\n\n<p style='color: white'><small>" + \
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

# Создание CLI/HTML графиков.
        if not Windows:
            print("")
            console.rule(f"[bold blue]graph in CLI[/bold blue]", characters="#")
            print("")
        for html_file in [[Maximum_stars_in_date, cumulative_datestars], f"{path}/all_gone_stars.html"]:
            data = agregated_date(html_file)
            if isinstance(html_file, list):
                html_file = f"{path}/all_new_stars.html"
            generate_plots(data, html_file, months_stars, years_stars, hours_stars, mean_year, mean_days, dif_date)

# Искать пересеченных пользователей.
        common_users_found = cross_user_detect(set(lst_new))

        try:
            webbrowser.open(f"file://{path}/report.html")
        except Exception:
            console.print("[bold red]It is impossible to open the web browser due to problems with the operating system.")

    finish(token, stars, report=True)
    win_exit()

# Arbeiten.
if __name__ == '__main__':
    main_cli()
