## Shotstars

********
**v0.2**
********

— You can install the Shotstars package using pip ($ pip install shotstars).

— The script's operation has been accelerated several times due to task parallelization.

— An title metric has been added to the html-report:
  accumulation of “Gone Stars/Dates” for the entire time of scans.

— Changed the appearance of CLI tables. In CLI, the estimated waiting time in minutes has been 
  added to the limit removal date/time. Updated the progress function. The appearance of the html
  report has been redesigned.
  
— Expanded checking for URL input errors, for example, if the user specified a non-existent or
  deleted repository for parsing or tried to scan a repository with more than 6K+ stars, etc.

— Added new functionality to the html report: display of accumulated data for all "new/gone stars"
  broken down by dates; summary calculation of "new/gone stars/date" in the header; and most 
  importantly, a count of duplicate "usernames" that have repeatedly added or removed stars in the
  monitored repository is kept.

— Added a new metric: the real date of creation of the project (sometimes the date of creation of 
  the project can be faked using commits, deceiving users, Shotstars cannot be deceived).
  The html report also added: rating; the real date of creation of the project and description of 
  the project (if present).
  
— Added random "User-Agent" for http requests.

— In case of using old version of Python3.7 on OS Android/Termux or due to limitations of 
  new versions of OS Android fast processes are replaced by safe slow threads.
=================================================================================================

********
**v0.1**
********
— Collected ready-made “shotstars” assemblies for OS GNU/Linux; OS Windows; OS Android (Termux),
  i.e. no libs or Python required.

— Parsing user's stars with checking for errors and restrictions.

— Session support; correct software stop (ctrl +c); some decorations (progress, CLI zebra tables)

— Reports in CLI and HTML formats, including date calculations.

— Support for simulating results, a documented software hack - or a side feature designed to test
  the script on dead/stable repositories without star movement.
=================================================================================================
