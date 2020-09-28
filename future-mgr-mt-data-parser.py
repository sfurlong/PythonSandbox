# This Python Script Used this Curl Script to get OData from The Future Manager Program
# curl -v --user "furlons@amazon.com:Skitaos1" -H "Accept:application/json" "https://admin.mindtickle.com/Odata.svc/LearnerModulePerformances?%24filter=SeriesName%20eq%20%27Americas%20Future%20Manager%27" > future-mgr-mt-rpt.xml
#from typing import List, Any

import pandas as pd
import xml.etree.ElementTree as et
import numpy as np
#import matplotlib.pyplot as plt
import sys

# Dataframe print settings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



#print ("The script has the name %s" % (sys.argv[1]))

# Read XML File
# Make sure to remove this namespace(xmlns="http://www.w3.org/2005/Atom" ) from the <feed> element in the file, or the python won't work
xmlTree = et.parse("/Users/furlons/checklists.xml")  # create an ElementTree object
root = xmlTree.getroot()
i = 0
ns = "{http://schemas.microsoft.com/ado/2007/08/dataservices}" # Another garbage namespace in the odata file
rowVals = []
rows = []
colNames = []
data = pd.DataFrame()
for child in root.findall("./entry"):
    i=i+1
    for entryNodes in child.iter():
        if entryNodes.tag.startswith(ns):
            colName = entryNodes.tag[len(ns):]
            colVal = entryNodes.text
            rowVals.append(colVal)
            print(colName + ": " + colVal)
            #if i == 1:
                #colNames:.append(colName)
    #rows.append(rowVals.copy())
    #rowVals.clear()

#df = pd.DataFrame(rows, columns=colNames:)
#print(df.shape)

#df = df[df.LearnerModuleState != 'deactivated']
#df = df.drop(['UserId', 'SeriesId', 'ModuleId', 'Version', 'LearnerModuleState'], axis=1)
#df["HasCompleted"].fillna(0, inplace=True) # Fill nulls with 0
#df["HasCompleted"].replace({'false':0, 'true':1}, inplace=True)
#df["HasStarted"].fillna(0, inplace=True) # Fill nulls with 0
#df["HasStarted"].replace({'false':0, 'true':1}, inplace=True)

#print(df)
#df.to_csv('/Users/furlons/future-mgr-mt-rpt.csv')
