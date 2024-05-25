# shotstars
A tool to track waning stars on Github.  

<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/Termux%20logo.png" />

The purpose of the “shotstars” script is to find accounts from which they once gave stars to repositories,  
but then they were removed and provide such an analysis in a human-readable form (it doesn’t matter,  
you can scan both your own and other people’s projects), as a result, try to do what it doesn’t do Github by default.  
The secondary function of the software is to monitor the thrown stars also at a selected period of time.  

**Native Installation**  
```
pip install requests rich
python shot_stars.py
```

**Ready-made builds are provided for OS GNU/Linux & Windows & Termux (Python is not required)**  
⬇️[Download shotstars](https://github.com/snooppr/shotstars/releases "download a ready-made assembly for Windows; GNU/Linux or Termux")  

 ---

<details>
<summary> 🔵 Screenshot gallery</summary>  

### 1. shotstars for windows 7  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/shotstars%20Win.png" />  

 ---

### 2. shotstars for GNU/Linux  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/shotstars%20Linux.gif" />  

 ---

### 3. shotstars for Termux html report  
<img src="https://raw.githubusercontent.com/snooppr/shotstars/main/images/html%20report.png" />  

 ---

</details>

"shotstars" supports simulation of results. To simulate the process, the user must scan the new repository once,   
adding it to the database; randomly delete and add any lines to a file (OS GNU/Linux and Termux)  
`/home/{user}/ShotStars/results/{repo}/new.txt`  
(OS Windows)  
`C:\Users\{User}\AppData\Local\ShotStars\result\{repo}\new.txt`;  
run a second scan of the same repository.  
