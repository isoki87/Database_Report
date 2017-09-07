#!/usr/bin/env python
import psycopg2


# This function repackages our SQL results(tuple)
def presentFirstAndSecondRep(results):
    for row in results:
        print str(row[0]) + "  -  " + str(row[1]) + " views."


# This funtion handles the query and comms with the db
def topThreeArticlesInternal():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = ('SELECT title, views FROM titleRanking LIMIT 3;')
    c.execute(query)
    return c.fetchall()
    db.close()


# This function answers the first question
def topThreeArticles():
    print "The top three articles read in July 2016 are:"
    results = topThreeArticlesInternal()
    presentFirstAndSecondRep(results)
    print "\n"


# This function handles the query and comms with the db
def rankAuthorsInternal():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = ('SELECT authors.name, SUM(titleRanking.views) AS views '
             'FROM authors, titleRanking '
             'WHERE authors.id = titleRanking.author '
             'GROUP BY authors.name '
             'ORDER BY views DESC;'
             )
    c.execute(query)
    return c.fetchall()
    db.close()


# This function answers the second question
def rankAuthors():
    print ("Below is the list of authors who received page views"
           " on their articles in July 2016:")
    results = rankAuthorsInternal()
    presentFirstAndSecondRep(results)
    print "\n"


# This function repackages our SQL results(tuple)
def presentThirdRep(results):
    end = " percent of total requests as erroneous."
    for row in results:
        print str(row[0]) + " , with " + str(row[1] * 100) + end


# This function handles the query and comms with the db
def errorDayInternal():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = ('SELECT ePD.days,'
             'ePD.occurances/CAST(tEPD.events AS FLOAT) AS eR '
             'FROM ePD, tEPD '
             'WHERE ePD.days = tEPD.days '
             'AND ePD.occurances/CAST(tEPD.events AS FLOAT)>= 0.01;'
             )
    c.execute(query)
    return c.fetchall()
    db.close()


# This function answers the third question
def errorDay():
    print ("Below are the day(s) when more than 1%"
           " of the view requests led to errors:")
    results = errorDayInternal()
    presentThirdRep(results)


# The main function contains the three answers, as well as intro and outro
def main():
    print "Welcome! The following report has been prepared for you:\n"
    topThreeArticles()
    rankAuthors()
    errorDay()
    print "End of report, thank you for your time! \n"


main()
