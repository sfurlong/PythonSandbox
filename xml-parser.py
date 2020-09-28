# This Python Script Used this Curl Script to get OData from The Future Manager Program
# curl -v --user "furlons@amazon.com:Skitaos1" -H "Accept:application/json" "https://admin.mindtickle.com/Odata.svc/LearnerModulePerformances?%24filter=SeriesName%20eq%20%27Americas%20Future%20Manager%27" > future-mgr-mt-rpt.xml
#from typing import List, Any

import pandas as pd
import xml.etree.ElementTree as et
import csv
import numpy as np
#import matplotlib.pyplot as plt
import sys

# Dataframe print settings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

ns = "{http://schemas.microsoft.com/ado/2007/08/dataservices}" # Another garbage namespace in the odata file

def parseXML(xmlfile):
    # create element tree object
    tree = et.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall("./entry"):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item.iter():

            # special checking for namespace object content:media
            if child.tag.startswith(ns):
                colName = child.tag[len(ns):]
                colVal = child.text
                news[colName] = colVal
#            else:
#                news[child.tag] = child.text.encode('utf8')

                # append news dictionary to news items list
        newsitems.append(news)

        # return news items list
    return newsitems


def savetoCSV(newsitems, filename, fields):
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)

checklistXMLFileName = '/Users/furlons/fm-checklist-tracking-092320.xml'
checklistCSVFileName = '/Users/furlons/fm-checklist-tracking-092320.csv'
fmCohortCSVFileName = '/Users/furlons/fm-cohort.csv'
finalMetricsFileName = '/Users/furlons/fm-checklist-tracking-092320-final.csv'
fields = ['ModuleName', 'TaskName', 'CompletionStatus', 'LearnerEmailId', 'LearnerName', 'Version', 'LatestReattemptNo',
          'UserId', 'Score', 'TaskId', 'MaxScore', 'ModuleId']

# parse xml file
xmlStuff = parseXML(checklistXMLFileName)

# specifying the fields for csv file
# store news items in a csv file
savetoCSV(xmlStuff, checklistCSVFileName, fields)

checklistDF = pd.read_csv(checklistCSVFileName)
cohortDF = pd.read_csv(fmCohortCSVFileName)

df = pd.merge(cohortDF, checklistDF, left_on='Participant Alias', right_on='LearnerEmailId', how='left')
print(df.shape)
print(df)
#savetoCSV(df, finalMetricsFileName, fields)

