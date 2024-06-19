# 💫 Shotstars
A tool to track waning stars on Github.  

> [!IMPORTANT]  
>Github does not provide users with statistics on disappearing stars in the repository. "Shotstars" is trying to resolve this issue and provide such information to the user.  

<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/Termux%20logo.png" />

The purpose of the “Shotstars” script is to find accounts from which they once gave stars to repositories,  
but then they were removed and provide such an analysis in a human-readable form (it doesn’t matter,  
you can scan both your own and other people’s projects), as a result, try to do what it doesn’t do Github by default.  
The secondary function of the software is to monitor the thrown stars also at a selected period of time.  

 ---

## ⌨️ Native Installation  
```
pip install requests rich
python shot_stars.py
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
There are restrictions from Github 【6000 stars/hour from one IP address】, repositories with more than 6K stars do not physically make sense to scan.  

 ---

<details>
<summary> 👈 Screenshot gallery </summary>  

### 1. shotstars for windows 7  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/shotstars%20Win.png" />  


### 2. shotstars for GNU/Linux  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/shotstars%20Linux.gif" />  


### 3. shotstars for Termux html report  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/html%20report.png" />  

</details>

 ---

## 🇷🇺 TL;DR  
Github не предоставляет пользователям статистику по исчезающим звездам в репозитории. "Shotstars" пытается решить этот вопрос и предоставить такую информацию пользователю. Существуют ограничения со стороны Github 【**6000 звезд/час** с одного IP адреса】, репозитории с более 6К звезд не имеет физического смысла сканировать. 
