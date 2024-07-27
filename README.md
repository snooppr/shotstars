# 💫 Shotstars
A tool to track waning stars on Github.  

> [!IMPORTANT]  
>Github does not provide users with statistics on disappearing stars in the repository. "Shotstars" is trying to resolve this issue and provide such information to the user.  

<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/CLI.png" />

The purpose of the “Shotstars” tool is to find accounts from which they once gave stars to repositories,  
but then they were removed and provide such an analysis in a human-readable form (it doesn’t matter,  
you can scan both your own and other people’s projects), as a result, try to do what it doesn’t do Github by default.  
The secondary function of the software is to monitor the thrown stars also at a selected period of time.  

 ---

## ⌨️ Native Installation  
[![Downloads](https://static.pepy.tech/badge/shotstars)](https://pepy.tech/project/shotstars)  

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

<details>
<summary> 👈👈 Screenshot gallery </summary>  

### 1. Shotstars for Windows 7  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/shotstars%20Win.png" />  


### 2 Shotstars HTML-report  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/html-report.png" />  


### 3 Shotstars for Android/Termux  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/Termux.png" />  


### 4 Shotstars Limit Github/API  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/Limit.png" />  


### 5 Shotstars Scan History
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/scan_history.png" />  

</details>

 ---

## 🇷🇺 TL;DR  
Github не предоставляет пользователям статистику по исчезающим звездам в репозитории.
"Shotstars" пытается решить этот вопрос и предоставить такую информацию пользователю.
Утилита также отслеживает прибавление звезд, аккумулирует результаты/статистику и мониторит дублирующую активность username's.
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
