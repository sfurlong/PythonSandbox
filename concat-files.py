import os
import sys
import glob
import zipfile
import pandas as pd


pathName = "/Users/furlons/scratchdir/"
outFileName = "all-fm-surveys.csv"  # type: str
os.chdir(pathName)

#Unzip all the survey files
for filename in glob.glob("*.zip"):
    print(os.path.join(pathName, filename))
    with zipfile.ZipFile(pathName + filename, 'r') as zip_ref:
        zip_ref.extractall(pathName)
        os.remove(filename)

#Combine all the survey files into a new file
#try :
open(pathName + outFileName, 'a').close()
with open(pathName + outFileName, 'w') as outfile:

    for filename in glob.glob("*.csv"):
        #skip the output file
        if filename == outFileName:
            continue
        print(pathName + filename)
        with open(pathName + filename) as infile:
            data = infile.read()
            #print(data)
            outfile.write(data)
#except:
#    print("Oops!", sys.exc_info()[0], "occurred.")

#Read the Combined file into a dataframe
df = pd.read_csv(pathName + outFileName)
print(df.shape)
#Drop unnecessary columns
df = df.drop(df.loc[:, 'K Score':'Area Leader Email Email ID'].columns, axis=1)
df = df.drop(df.loc[:, 'Like/Dislike':'Max Score'].columns, axis=1)
df = df.drop(columns=['Content Type', 'Topic Name', 'Completion State'])
print(df.shape)
#Replace some non-numeric values so we can do calculations
df.replace(to_replace ='["5"]', value ="5", inplace=True)
df.replace(to_replace ='["5 - Highest"]', value ="5", inplace=True)
df.replace(to_replace ='["4"]', value ="4", inplace=True)
df.replace(to_replace ='["3"]', value ="3", inplace=True)
df.replace(to_replace ='["2"]', value ="2", inplace=True)
df.replace(to_replace ='["1"]', value ="1", inplace=True)
df.replace(to_replace ='["Strongly Agree"]', value ="5", inplace=True)
df.replace(to_replace ='["Agree"]', value ="4", inplace=True)
df.replace(to_replace ='["Neutral"]', value ="3", inplace=True)
df.replace(to_replace ='["Disagree"]', value ="2", inplace=True)
df.replace(to_replace ='["Strongly Disagree"]', value ="1", inplace=True)
#Replace the week number
for idx in range(25):
    print(idx)
    df.replace(to_replace ='Week ' + str(idx) + ' Survey', value = str(idx), inplace=True)


#Filter Rows with '[]'; empty values.
idxNames = df[ (df['Responses'] == '[]') ].index
print(df.shape)
df.drop(idxNames , inplace=True)
print(df.shape)
print(idxNames)

df.to_csv(pathName + outFileName)


print ("done")
