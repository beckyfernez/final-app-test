# Reading csv from google sheets

# Google sheets import code adapted from https://www.youtube.com/watch?v=cnPlKLEGR7E

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import pandas as pd

scope2 = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds2 = ServiceAccountCredentials.from_json_keyfile_name('gu-dining-locations-cf538c00daae.json', scope2)

client2 = gspread.authorize(creds2)

workbook2 = client2.open("Georgetown Dining Reviews Data").sheet1

#creating a list
data2 = workbook2.get_all_records()

#pprint(data2)
#print(len(data2))

overall_list1=[]
overall_list2=[]
overall_list3=[]
overall_list4=[]
overall_list5=[]
overall_list6=[]
overall_list7=[]
overall_list8=[]
overall_list9=[]
overall_list10=[]
overall_list11=[]
overall_list12=[]
overall_list13=[]
overall_list14=[]

# we can maybe call a function to perform the average of a single row
for x in range (0, len(data2)):
    if data2[x]["location_id"]==1:
        average1 = (data2[x]["taste_score"]+data2[x]["health_score"]+data2[x]["service_score"]+data2[x]["portion_score"])/4
        overall_list1.append(average1)
    elif data2[x]["location_id"]==2:
        average2 = (data2[x]["taste_score"]+data2[x]["health_score"]+data2[x]["service_score"]+data2[x]["portion_score"])/4
        overall_list2.append(average2)

#print(overall_list1)
#print(type(overall_list1))

overall_score1 = sum(overall_list1)/len(overall_list1)
overall_score2 = sum(overall_list2)/len(overall_list2)
print(overall_score1, overall_score2)


#print(data2[0])
#print(data2[0]["health_score"])

# https://stackoverflow.com/questions/46448278/extracting-dictionary-items-embedded-in-a-list
#df = pd.DataFrame(data2)
#print(df)

#print(df["overall_score"])
#print(type(df["overall_score"]))

#sum = 0

#for x in range (0, len(data2)):
#    locationRow = df.iloc[x]
#    currentRow = df.iloc[x]
#    if locationRow["location_id"] == 1:
#        sum += currentRow["overall_score"]
#        print (currentRow["overall_score"]) # -- validating the correct rows collected
#        os_list = currentRow['overall_score'].tolist()

#print(os_list)

#print(sum)
#factor_list = list(df)
#factor_list.remove("review_id")
#factor_list.remove("location_id")
#print(factor_list)
#print(len(factor_list))

#df = df.astype({"taste_score":"int","health_score":"int", "service_score":"int", "portion_score":"int"})
#df["Average Score"] = (df["taste_score"]+df["health_score"]+df["service_score"]+df["portion_score"])
#print(df)

#df["Average Score"] = df.iloc[[2,3]].mean(axis=1)
#print(df)