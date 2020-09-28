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

df = pd.read_csv('/Users/furlons/Documents/SA Enablement/FutureMgr/Metrics/Future_Manager_Heatmap081020.csv')
print(df.shape)

#Drop unnecessary columns
#df = df.drop(df.loc[:, 'Groups':'Area Leader Email Email ID'].columns, axis=1)
df = df.drop(df.loc[:, 'Total Overdue':'% score'].columns, axis=1)
df = df.drop(df.loc[:, '% Certifications':'Total Certifications Received'].columns, axis=1)

#Replace some non-numeric values so we can do calculations
df.replace(to_replace ="Yet to Attempt", value ="0.0", inplace=True)
df.replace({'%': ''}, regex=True, inplace=True)
print(df)

#Loop Through all columns to calculate the Average consumption
columns = list(df)
idx = 0
s1 = pd.Series([])
cols = pd.Series([])
for i in columns:
       idx = idx + 1
       if idx > 10:
              df_mean = pd.to_numeric(df[i]).mean()
              s1 = s1.append(pd.Series([df_mean]))
              cols = cols.append(pd.Series([i]))
              print(i, df_mean)


print(s1)

#Try to chart this mess
#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.bar(cols, s1)
#plt.show()

df.to_csv('/Users/furlons/future-mgr-mt-rpt.csv')
