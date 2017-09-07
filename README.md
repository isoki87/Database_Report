#Final Project: Database Report Tool

 ---

**Overview and Design**

This program will perform queries on a newspaper database about its website usage to gain insights on the value of retaining its website.
This program is a python script which will begin running once it is called by the terminal. The script will introduce an intro message,
followed by three function calls to provide strategic insights on the website's value and possible improvement venues.
Each function calls will make a query to the database `news` to provide the most updated data. The script will then end on an outro message.

 ---

**File List**

* README.md
* report_tool.py
* sample_output.txt
* `news` database

 ---

**Before Running This File**

Prior to running the 'report_tool.py' file, please create the following views in the SQL console:

1. VIEW `pathRanking`:

This view aggregates each successful visits from users based on data from the `log` table and ranks the articles in descending order based on views, with the articles represented by their site paths.

```
CREATE VIEW pathRANKING AS SELECT path, count(ID) AS num FROM log WHERE status = '200 OK' AND path != '/' GROUP BY path ORDER BY num DESC;
```

2. VIEW `titleRanking`:

This view takes the `viewRanking` view and translates the site paths to each article's actual title, with the result being a ranked ordered of each articles with their titles based on views.

```
CREATE VIEW titleRanking AS SELECT articles.title, articles.author, pathRanking.num AS views from pathRanking, articles WHERE pathRanking.path LIKE '%'||articles.slug ORDER BY views DESC;
```

3. VIEW `ePD`:

This view, errors per day, aggregates the data from the `log` table and displays the number of errroneous requests made on each day.

```
CREATE VIEW ePD AS SELECT DATE(time) AS days, count(ID) AS occurances FROM log WHERE status != '200 OK' GROUP BY days ORDER BY days;
```

4. VIEW `tEPD`:

This view, total events per day, aggregates the data from the `log` table and displays the total number of requests made on each day.

```
CREATE VIEW tEPD AS SELECT DATE(time) AS days, count(ID) AS events FROM log GROUP BY days ORDER BY days;
```

---

**How to Run This File**

1. Navigate to the folder containing the files on your VM using the `cd` command followed by `ENTER` in your console.
2. Enter the command `ls` and press `ENTER` to ensure that all files in the File List are in the folder
3. Enter the command `python report_tool.py` followed by pressing `ENTER` to begin running the python script

---
