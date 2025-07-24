# 💫 𝕊𝕙𝕠𝕥𝕤𝕥𝕒𝕣𝕤
︻デt══━一🔥 · ·· *A unique and over fab tool to track stars on Github*.  

> [!IMPORTANT]  
> 𝕊𝕙𝕠𝕥𝕤𝕥𝕒𝕣𝕤 𝕔𝕒𝕟 𝕕𝕠 𝕥𝕙𝕚𝕟𝕘𝕤 𝕥𝕙𝕒𝕥 𝔾𝕚𝕥𝕙𝕦𝕓 𝕕𝕠𝕖𝕤𝕟'𝕥 𝕕𝕠 𝕓𝕪 𝕕𝕖𝕗𝕒𝕦𝕝𝕥.
>
> 𝕊𝕦𝕡𝕡𝕠𝕣𝕥𝕖𝕕 𝕆𝕊: 𝔾ℕ𝕌/𝕃𝕚𝕟𝕦𝕩; 𝕎𝕚𝕟𝕕𝕠𝕨𝕤 𝟟+; 𝔸𝕟𝕕𝕣𝕠𝕚𝕕/𝕋𝕖𝕣𝕞𝕦𝕩; 𝕞𝕒𝕔𝕆𝕊 (𝕚𝕟𝕥𝕖𝕣𝕞𝕚𝕥𝕥𝕖𝕟𝕥𝕝𝕪).  

<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/CLI.png" />  

Shotstars allows you to monitor any repository from the outside.  
For example, can a network user say: how many stars have been added or subtracted from some interesting GitHub repository in a month? *(IT hosting does not provide information on the decrease in stars, even to the owner of its own projects)*.  
Shotstars will care about and count specifically those GitHub users who have removed, added stars to any project; or set their profile to "private"; or even left the platform entirely. In addition to statistics, the tool allows you to identify repositories with fake stars.  

**Claimed functions:**  
- [X] Shotstars will help find and expose naked kings and their retinue *(fact: stars in some repositories are inflated).*  
- [X] Shotstars calculates parameters: aggressive marketing, trend, fake stars, peak of popularity and its date.  
- [X] Shotstars will calculate progress or regression over the last month *(median - trend in percentage change and average - calculated in fact in times).*  
- [X] Shotstars Shotstars will calculate the names of the months that had the most and the least stars *(mode / anti-mode)*, and will also display the entire history of stars by quartiles, a similar calculation is made by year.  
- [X] Shotstars will output the longest period of time without adding stars.  
- [X] Shotstars scans repositories for stars added and removed with statistics for a selected time period.  
- [X] Shotstars reports the real date of the repository *(fact: developers can declare/fake/change the date of their projects commits, but Shotstars will not fool them, the utility will display real numbers)*.  
- [X] Shotstars will show ~ the size of any public repository.  
- [X] Shotstars will also provide a short description of the repository.  
- [X] Shotstars offers a scan history with a selection of previously registered projects for quick checking.  
- [X] Shotstars generates CLI/HTML reports *(stats, time periods, duplicate user activity, urls and json)*.  
- [X] Shotstars creates graphs and histograms *(all star history by date, by month, by year, by hour, cumulative set of stars)*.  
- [X] Shotstars can simulate results, documented hack: a function designed to check the utility's operation *(to make sure)* on dead/stable repositories without moving stars.  
- [X] Shotstars finds users that overlap across Github projects, including those with hidden/private profiles.  
- [X] Shotstars calculates to the minute and displays the time when the github rescan restriction is lifted *(if token is not used)*.  
- [X] Shotstars is created for people and works out of the box, OS support: Windows7+, GNU/Linux, Android *(the user [does not need](https://github.com/snooppr/shotstars/releases): technical skills; registration/authorization on Github and even the presence of Python)*.  
- [X] Shotstars processes tasks with jet speed and for free *(cross-platform open source software, donations are welcome)*.  

 ---

## ⌨️ Native Installation  
![Static Badge](https://img.shields.io/badge/latest%20v4.5-430094?link=https%3A%2F%2Fraw.githubusercontent.com%2Fsnooppr%2Fshotstars%2Frefs%2Fheads%2Fmain%2Fchangelog)  


```
$ pip install shotstars
$ shotstars_cli
```

**Ready-made "Shotstars" builds are provided for OS GNU/Linux & Windows & Termux (Python is not required)**  
⬇️[Download Shotstars](https://github.com/snooppr/shotstars/releases "download a ready-made assembly for Windows; GNU/Linux or Termux")  

 ---

## 💾 Scan history  
In Shotstars the scan history is available, now you no longer need to enter or copy/paste the URL each time,
specify the keyword `his/history` instead of the repository url and select the previously scanned repository by number.

 ---

## 🌀 With Shotstars, users can also detect fake stars  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/refs/heads/main/images/anomalies_among_stars.png" />  
  
Example presumably of fake stars *(this repository was previously caught pirating)*. From the graph of spikes it is clear that in two weeks the repository gained +5K fake stars *(a couple of years later this repository stocked up on fake stars again).*  
  
Shotstars also offers a line chart: a cumulative set of stars.  
  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/refs/heads/main/images/anomalies_among_stars_cum.png" />  
  
Comparison of two repositories, cumulative set of stars. The upper screenshot is the usual movement of stars, the lower screenshot is the promotion of fake stars.  
  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/refs/heads/main/images/anomalies_among_stars_json.png" />  
  
For any repository, Shotstars will provide all users who have added stars, broken down by date, in json format, which means it's even easier to analyze anomalous peaks on the chart.  
  
Research on the promotion of fake stars **/** Исследование про накрутку фейковых звезд 
[RU](https://habr.com/ru/articles/723648/) / [RU_2](https://www.opennet.ru/opennews/art.shtml?num=62515) **|** 
[EN](https://dagster.io/blog/fake-stars) / [EN_2](https://arxiv.org/html/2412.13459v1)  

 ---

## ⚙️ Shotstars supports simulation of results  
Note that the HTML report is generated when the repository is rescanned. If the user needs to force a specific HTML report, simply enable star simulation. 👇  
A documented software hack - or side function designed to test the script on dead/stable repositories without star movement.  
To simulate the process, the user must scan the new repository once,   
adding it to the database; randomly delete and add any lines to a file  
(OS GNU/Linux and Termux):    
`/home/{user}/.ShotStars/results/{repo}/new.txt`  
(OS Windows):  
`C:\Users\{User}\AppData\Local\ShotStars\result\{repo}\new.txt`;  
run a second scan of the same repository.  

 ---

## ⛔️ Github restrictions  
There are restrictions from Github 【**6K stars/hour** from one IP address】, repositories with more than 6K stars do not physically make sense to scan.  
In Shotstars with Github token  you can [bypass the restrictions](https://github.com/snooppr/shotstars/issues/3) and scan repositories up to **500K stars/hour**.  
Steps to get a token *(free)*:  
1) register for an account on Github (if you don’t already have one);  
2) open your profile -> settings -> developer settings -> personal acces tokens -> generate new token;  
3) insert the resulting token (string) into in the field instead of 'None'  
GNU/Linux & Android/Termux::  
`/home/{user}/.ShotStars/results/config.ini`  
OS Windows::  
`C:\Users\{User}\AppData\Local\ShotStars\result\config.ini`.  

The Github token belongs to the user, is stored locally and is not transferred or downloaded anywhere.  
You can parse both your own and third-party repositories (by default, registration/authorization/token are not required).  

 ---

## 🇷🇺 TL;DR  
Shotstars позволяет следить со стороны <u>за любым публичным</u> репозиторием.  
Например, может ли пользователь сети сказать: сколько прибавилось или убавилось звезд у какого-нибудь интересного github-репозитория за месяц? *(IT-хостинг не предоставляет информацию по убыванию звезд, даже хозяину своих собственных проектов)*. Shotstars позаботится и вычислит конкретно тех github-пользователей, кто удалил, накинул звезды любому проекту, а то и вовсе удалился с платформы или перевёл профиль в режим "private". Кроме статистики, инструмент позволяет вычислять репозитории с фейковыми звездами.  

**Заявленные функции:**  
- [X] Shotstars поможет найти и разоблачить голых королей и их свиту *(факт: звезды в некоторых репозиториях накручивают)*.  
- [X] Shotstars рассчитывает параметры: агрессивный маркетинг, тренд, фейковые звезды, пик популярности и его дата.  
- [X] Shotstars рассчитает прогресс или регресс за последний месяц *(медиану — тенденцию в процентном изменении и среднее — рассчитанное по факту в разах).*  
- [X] Shotstars вычислит имена месяцев, в которых было всех больше и всех меньше получено звезд *(мода / анти-мода)*, а также выведет всю историю звезд по квартилям, аналогичный расчет и по годам.  
- [X] Shotstars выведет самый протяженный период времени без прибавления звезд *(черная полоса)*.  
- [X] Shotstars проверяет репозитории на предмет прибавления и убавления звезд со статистикой за выбранный период времени.  
- [X] Shotstars сообщает реальную дату создания репозитория *(факт: разработчики могут заявлять/подделывать/изменять дату создания своих проектов и коммитов, но Shotstars им не обмануть, утилита отобразит реальные цифры)*.  
- [X] Shotstars покажет ~ размер любого публичного репозитория.  
- [X] Shotstars также предоставит краткое описание репозитория.  
- [X] Shotstars предлагает для быстрой проверки историю сканирований с выбором ранее учтенных проектов.
- [X] Shotstars генерирует CLI/HTML отчеты *(статистика, периоды времени, дублирующая активность пользователей, url's и json)*.  
- [X] Shotstars создает графики и гистограммы *(вся история звезд по дате/времени: по месяцам, по годам, по часам, кумулятивный набор звезд)*.  
- [X] Shotstars умеет имитировать результаты, задокументированный хак: функция, призванная проверить работу утилиты *(удостовериться)* на мертвых/стабильных репозиториях без движения звезд. 
- [X] Shotstars находит пересекающихся у Github-проектов пользователей, в т.ч. и тех, у кого профиль скрыт/приватный.  
- [X] Shotstars рассчитывает с точностью до минуты и отображает время снятия github-ограничения на повторные сканирования *(если не используется token)*.  
- [X] Shotstars создан для людей и работает из коробки, поддержка OS: Windows7+, GNU/Linux, Android *(от пользователя [не требуются](https://github.com/snooppr/shotstars/releases): владения техническими навыками; регистрация/авторизация на Github и даже наличие Python)*.  
- [X] Shotstars отрабатывает задачи с реактивной скоростью и задаром *(open source, кроссплатформенность, донаты приветствуются)*.  

Существуют ограничения со стороны Github 【**6K звезд/час** с одного IP адреса】, репозитории с более 6К звезд не имеет физического смысла сканировать.  
В Shotstars с Github-токеном [ограничения можно обойти](https://github.com/snooppr/shotstars/issues/3) и сканировать репозитории до **500K звезд/час**.  
Шаги для получения токена *(бесплатный)*:  
1) зарегистрируйте аккаунт на Github (если у вас его еще нет);  
2) откройте профиль -> settings -> developer settings -> personal acces tokens -> generate new token;  
3) полученный токен (строку) вставьте в поле заместо 'None' в файл  
OS GNU/Linux & Android/Termux::  
`/home/{user}/.ShotStars/results/config.ini`  
OS Windows::  
`C:\Users\{User}\AppData\Local\ShotStars\result\config.ini`.  

Github-токен принадлежит пользователю, хранится локально и никуда не передается и не скачивается.  
Парсить можно, как свои, так и сторонние репозитории *(по умолчанию регистрация/авторизация/токен не требуются)*.  

В Shotstars доступна история сканирований, не нужно теперь каждый раз вводить или копи/пастить url,
укажите вместо url репозитория ключевое слово `his/history` и выберите цифрой ранее сканируемый репозиторий.  

Обратите внимание, что HTML-отчет создается при повторном сканировании репозитория. Если пользователю требуется принудительно получить особенный HTML-отчет, просто включите [симуляцию](https://github.com/snooppr/shotstars#%EF%B8%8F-shotstars-supports-simulation-of-results) звезд.  

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
Shotstars is awesome, it sees everything. Github says the repository hasn't had any commits in a month, but there has been some subtle activity, like PR updates, etc. (by the way, commit rewriting and date manipulation is also easily detected).  


*7 Shotstars finds users that overlap across Github projects, including those with hidden/private profiles*  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/cross.png" />  


*8 Shotstars generates HTML-CLI timelines of a repository's star history, both new and gone.*  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/graph.png" />  


<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/graphs.png" />  
Comparison of two repositories based on stellar history. It is clear that the peak of popularity of the first repository has long passed, the development has gone into decline (forks). The second repository is a legend and is steadily gaining popularity.  


<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/graphs2.png" />  
Starry hour. Repository from location RU. It is clear that its audience is European, in the morning hours, at night, much fewer stars come.  

 ---

## 💡 Explanation of some metrics  

+ **"Date-update (including hidden update)"** — The metric displays two things: firstly, if a developer pushes a commit and then completely erases the commits from the server and/or overwrites them, Shotstars will know about it and tell you; secondly, the metric will be updated if, for example, there are no pushes, but a pull request is cancelled/added, etc.  

+ **"Peak-stars-in-date"** — The metric displays the date (per day) on which the maximum number of stars was received.  

+ **"The-trend-of-adding-stars (forecasting)"** — The metric displays the predicted increase in stars per day based on the repository history and algorithm.  

+ **"Most-of-stars-month / Smallest-of-stars-month"** — The metric displays the calculation of two months in the entire history of the repository (the most profitable month by stars and the month with the least stars, mode / anti-mode).  

+ **"Distribution-of-stars-by-month"** — Calculation of stars by month for the entire history of the repository (may include rare phenomenon: private stars, when the sum of all stars ≠ 'GitHub-rating'), coloring of the range of stars by quartiles (green: x > Q3); (yellow: Q1 <= x <= Q3); (red: x < Q1), The font size also decreases from Q3...Q1. Groups are not always arranged "3/6/3", for example, the groups of the "Shotstars" repository are arranged "3/4/5". The characteristic is calculated when the age of the repository is at least one month.  

+ **"Distribution-of-stars-by-year"** — Same as the metric '"Distribution-of-stars-by-month"', but the calculation is not by month, but by year, and the metric does not display the number of private stars. The characteristic is calculated when the age of the repository is at least one year.  

+ **"Longest-period-without-add-stars"** — The metric displays the longest time span when no stars were submitted to the repository, i.e. every day in a row there were 0 stars (black streak).  

+ **"Median-percentage-change"** — The metric reflects the average trend in stars (i.e. does not take into account sharp fluctuations in stars, such as fake stars or a sharp drop/popularity from the media), calculated as a percentage, the ratio of the last month to the penultimate month. Positive numbers are easy to interpret, negative ones are not. The simplest example: a user scans a repository at the beginning of January (in November, the repository received +30 stars, and in December, +60 stars), the metric will display "100%"; if everything was the other way around (in November, the repository received +60 stars, and in December, +30 stars), the metric will display "-50%" (not "-1~~00%"~~). The characteristic is calculated when the repository is at least two months old.  

+ **"Average-change-in-fact"** — Unlike the "Median-percentage-change" metric, it reflects not the average trend, but the real state of affairs, i.e. the arithmetic mean and takes into account all fluctuations and dips in stars for the same period (the ratio of the last month to the penultimate month), but is calculated not in percentages, but in times and units (stars). Example: in November the repository added +30 stars, in December +60 stars, then the metric will display - "2 times (30 stars)" and vice versa, if in November +60 stars, and in December +30 stars, then the metric will display - "-2 times (-30 stars)". The characteristic is calculated when the repository is at least two months old.  

+ **"Aggressive-marketing"** — The metric accepts the following values: "—"; "Low"; "Medium"; "High"; "Hard"; "Hard+". "—" means that the repository consistently receives or does not receive stars, without jumps, usually such repositories do not care about their popularity, are rarely/not mentioned in the media. "Low"; "Medium"; "High" — these repositories are repeatedly mentioned in the media, the movement of stars is uneven, they can attract hundreds of stars per day, the popularity of the repositories is high. "Hard" — frequent and frantic, uneven movement of stars, i.e. unnatural, the promotion of fake stars. "Hard+" — usually this is multiple promotion of fake stars in large quantities, i.e. more than once. The characteristic is calculated when the repository is at least two months old.  

+ **"Fake-stars"** — The metric takes the following values: "Yes"; "Yes, multiple attempts to promote fake stars". In the first case, this could be a one-time, but large promotion of fake stars or regular promotion of stars little by little. In the second case, these are obvious and multiple promotions of fake stars. The characteristic is calculated when the repository is at least two months old.  

+ **"New stars"** — New stars for the repository from the penultimate scan to the last scan. The characteristic is calculated based on the frequency of repository scans. For the graph, the actual parsing is calculated, i.e. the stars received for the entire history of the repository.  

+ **"Gone stars"** — The metric displays those users: who removed their stars from the repository; or deleted their account from the Github platform; or switched their profile to "private" mode - such a profile, like a deleted one, can lead to "404" by link, i.e. Github (not always) completely hides all user activity and their personal page, but such an account can conduct activity that is almost never displayed anywhere except by the account owner (for example, only reactions are displayed). Gone stars for the repository for the period from the penultimate scan to the last scan. The characteristic is calculated based on the frequency of repository scans.  

+ **"cross-users"** — The metric only displays those overlapping users that overlap in the scanned repositories relative to a specific scanned repository.  
