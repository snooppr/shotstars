# 💫 Shotstars
A unique and over fab tool to track stars on Github.  

> [!IMPORTANT]  
>Shotstars can do things that Github doesn't do by default.  

<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/CLI.png" />  

Shotstars allows you to monitor any repository from the outside.  
For example, can a network user say: how many stars have been added or subtracted from some interesting GitHub repository in a month? *(IT hosting does not provide information on the decrease in stars, even to the owner of its own projects)*.  
Shotstars will take care of and calculate specifically those GitHub users who have deleted or added stars to any project, 
or even completely left the platform.  

**Claimed functions:**  
- [X] Shotstars scans repositories for stars added and removed with statistics for a selected time period.  
- [X] Shotstars reports the real date of the repository *(fact: developers can declare/fake/change the date of their projects commits, but Shotstars will not fool them, the utility will display real numbers)*.  
- [X] Shotstats will show ~ the size of any public repository.  
- [X] Shotstars will also provide a short description of the repository.  
- [X] Shotstars offers a scan history with a selection of previously registered projects for quick checking.  
- [X] Shotstars generates CLI/HTML reports *(stats, time periods, duplicate user activity, urls)*.  
- [X] Shotstars can simulate results, documented hack: a function designed to check the utility's operation *(to make sure)* on dead/stable repositories without moving stars.  
- [X] Shotstars is created for people and works out of the box, OS support: Windows7+, GNU/Linux, Android *(the user [does not need](https://github.com/snooppr/shotstars/releases): technical skills; registration/authorization on Github and even the presence of Python)*.  
- [X] Shotstars processes tasks with jet speed and for free *(cross-platform open source software, donations are welcome)*.  

 ---

## ⌨️ Native Installation  
[![Downloads](https://static.pepy.tech/badge/shotstars)](https://pepy.tech/projects/shotstars?versions=1.1%2C1.2%2C1.3%2C1.4&timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=table)  

```
$ pip install shotstars
$ shotstars_cli
```

**Ready-made "Shotstars" builds are provided for OS GNU/Linux & Windows & Termux (Python is not required)**  
⬇️[Download Shotstars](https://github.com/snooppr/shotstars/releases "download a ready-made assembly for Windows; GNU/Linux or Termux")  

 ---

## ⚙️ Shotstars supports simulation of results  
A documented software hack - or side function designed to test the script on dead/stable repositories without star movement.  
To simulate the process, the user must scan the new repository once,   
adding it to the database; randomly delete and add any lines to a file  
(OS GNU/Linux and Termux):    
`/home/{user}/ShotStars/results/{repo}/new.txt`  
(OS Windows):  
`C:\Users\{User}\AppData\Local\ShotStars\result\{repo}\new.txt`;  
run a second scan of the same repository.  

 ---

## ⛔️ Github restrictions  
There are restrictions from Github 【**6K stars/hour** from one IP address】, repositories with more than 6K stars do not physically make sense to scan.  
In Shotstars with Github token  you can [bypass the restrictions](https://github.com/snooppr/shotstars/issues/3) and scan repositories up to **500K stars/hour**.  
Steps:  
1) register for an account on Github (if you don’t already have one);  
2) open your profile -> settings -> developer settings -> personal acces tokens -> generate new token;  
3) insert the resulting token (string) into in the field instead of 'None'  
GNU/Linux & Android/Termux::  
`/home/{user}/ShotStars/results/config.ini`  
OS Windows::  
`C:\Users\{User}\AppData\Local\ShotStars\result\config.ini`.  

The Github token belongs to the user, is stored locally and is not transferred or downloaded anywhere.  
You can parse both your own and third-party repositories (by default, registration/authorization/token are not required).  

 ---

## 💾 Scan history  
In Shotstars the scan history is available, now you no longer need to enter or copy/paste the URL each time,
specify the keyword `his/history` instead of the repository url and select the previously scanned repository by number.

 ---

## 🇷🇺 TL;DR  
Shotstars позволяет следить со стороны <u>за любым</u> репозиторием.  
Например, может ли пользователь сети сказать: сколько прибавилось или убавилось звезд у какого-нибудь интересного github-репозитория за месяц? *(IT-хостинг не предоставляет информацию по убыванию звезд, даже хозяину своих собственных проектов)*. Shotstars позаботится и вычислит конкретно тех github-пользователей, кто удалил или накинул звезды любому проекту, а то и вовсе удалился с платформы.

**Заявленные функции:**  
- [X] Shotstars проверяет репозитории на предмет прибавления и убавления звезд со статистикой за выбранный период времени.  
- [X] Shotstars сообщает реальную дату создания репозитория *(факт: разработчики могут заявлять/подделывать/изменять дату создания своих проектов и коммитов, но Shotstars им не обмануть, утилита отобразит реальные цифры)*.  
- [X] Shotstats покажет ~ размер любого публичного репозитория.  
- [X] Shotstars также предоставит краткое описание репозитория.  
- [X] Shotstars предлагает историю сканирований с выбором ранее учтенных проектов для быстрой проверки.
- [X] Shotstars генерирует CLI/HTML отчеты *(статистика, периоды времени, дублирующая активность пользователей, url's)*.  
- [X] Shotstars умеет имитировать результаты, задокументированный хак: функция, призванная проверить работу утилиты *(удостовериться)* на мертвых/стабильных репозиториях без движения звезд.  
- [X] Shotstars создан для людей и работает из коробки, поддержка OS: Windows7+, GNU/Linux, Android *(от пользователя [не требуются](https://github.com/snooppr/shotstars/releases): владения техническими навыками; регистрация/авторизация на Github и даже наличие Python)*.  
- [X] Shotstars отрабатывает задачи с реактивной скоростью и задаром *(open source, кроссплатформенность, донаты приветствуются)*.  

Существуют ограничения со стороны Github 【**6K звезд/час** с одного IP адреса】, репозитории с более 6К звезд не имеет физического смысла сканировать.  
В Shotstars с Github-токеном [ограничения можно обойти](https://github.com/snooppr/shotstars/issues/3) и сканировать репозитории до **500K звезд/час**.  
Шаги:  
1) зарегистрируйте аккаунт на Github (если у вас его еще нет);  
2) откройте профиль -> settings -> developer settings -> personal acces tokens -> generate new token;  
3) полученный токен (строку) вставьте в поле заместо 'None' в файл  
OS GNU/Linux & Android/Termux::  
`/home/{user}/ShotStars/results/config.ini`  
OS Windows::  
`C:\Users\{User}\AppData\Local\ShotStars\result\config.ini`.  

Github-токен принадлежит пользователю, хранится локально и никуда не передается и не скачивается.  
Парсить можно, как свои, так и сторонние репозитории *(по умолчанию регистрация/авторизация/токен не требуются)*.  

В Shotstars доступна история сканирований, не нужно теперь каждый раз вводить или копи/пастить url,
укажите вместо url репозитория ключевое слово `his/history` и выберите цифрой ранее сканируемый репозиторий.  

<details>
<summary>Shotstars это скрипт или ПО?</summary>

Существует ли чёткая грань между скриптом и программой? С таким опросом обратился разработчик к IT-сообществу Хабр.  

<img src="https://habrastorage.org/webt/vj/rq/kp/vjrqkptejw8lvhbi1oj8ibkqcn4.jpeg" />  

</details>

 ---

## 🔻 Screenshot gallery  

*1. Shotstars for Windows 7*  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/shotstars%20Win.png" />  


*2 Shotstars HTML-report*  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/html-report.png" />  


*3 Shotstars for Android/Termux*  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/Termux.png" />  


*4 Shotstars Limit Github/API (If you don't use the free token)*  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/Limit.png" />  


*5 Shotstars Scan History*
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/scan_history.png" />  


*6 Shotstars Discovers Hidden Developer Activity*
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/hidden update.png" />  
Shotstars is amazing, it sees everything. Github says that the repository hasn't been committed for a month, but the commits were made secretly (rewriting and manipulating commit dates, this is a question for the repository developer: why do they do this).  
