# Reading csv from google sheets

# Google sheets import code adapted from https://www.youtube.com/watch?v=cnPlKLEGR7E

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# delete later if we don't use df
import pandas as pd

scope2 = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds2 = ServiceAccountCredentials.from_json_keyfile_name('gu-dining-locations-cf538c00daae.json', scope2)

client2 = gspread.authorize(creds2)

workbook2 = client2.open("Georgetown Dining Reviews Data").sheet1

# List of dictionaries (all values corresponsing to the csv file)
data2 = workbook2.get_all_records()

print (data2)

# List of review averages for each location
overall_list1=[]
overall_list2=[]

# we can maybe call a function to perform the average of a single row (refactoring) (maybe also create a list of list)
for review_number in range (0, len(data2)):
    if data2[review_number]["location_id"]==1:
        average = (data2[review_number]["taste_score"]+data2[review_number]["health_score"]+data2[review_number]["service_score"]+data2[review_number]["portion_score"])/4
        overall_list1.append(average)
    elif data2[review_number]["location_id"]==2:
        average = (data2[review_number]["taste_score"]+data2[review_number]["health_score"]+data2[review_number]["service_score"]+data2[review_number]["portion_score"])/4
        overall_list2.append(average)

print(overall_list1)
print(overall_list2)

# call function here or use a for loop

# calculate averages of for each location review avg.
overall_score1 = sum(overall_list1)/len(overall_list1)
overall_score2 = sum(overall_list2)/len(overall_list2)
print("overall average score for location 1:", overall_score1)
print("overall average score for location 2:", overall_score2)

#collective_list=[]
#average_list = []
#
#for location_id in range (1, 14):
#    for review_number1 in range (0, len(data2)):
#        if data2[review_number1]["location_id"]==location_id:
#            average = (data2[review_number1]["taste_score"]+data2[review_number1]["health_score"]+data2[review_number1]["service_score"]+data2[review_number1]["portion_score"])/4
#            average_list.append(average)
#            pprint(average_list)
#            collective_list.append(average_list)
#            average_list.clear
#


#pprint(collective_list)


#print(data2[0])
#print(data2[0]["health_score"])

# https://stackoverflow.com/questions/46448278/extracting-dictionary-items-embedded-in-a-list
df = pd.DataFrame(data2)
print(df)

#print(df["overall_score"])
#print(type(df["overall_score"]))

#sum = 0
#
#for x in range (0, len(data2)):
#    #locationRow = df.iloc[x]
#    currentRow = df.iloc[x]
#
#    if currentRow["location_id"] == 1:
#        df["Average Score"] = currentRow["taste_score"]+currentRow["health_score"]+currentRow["service_score"]+currentRow["portion_score"]
        #sum += currentRow["overall_score"]
        #print (currentRow["overall_score"]) # -- validating the correct rows collected
        #os_list = currentRow['overall_score'].tolist()
        #os_list = average.tolist()
        
        


#print(os_list)

#print(sum)
#factor_list = list(df)
#factor_list.remove("review_id")
#factor_list.remove("location_id")
#print(factor_list)
#print(len(factor_list))


#df = df.astype({"taste_score":"int","health_score":"int", "service_score":"int", "portion_score":"int"})
df["Average Score"] = (df["taste_score"]+df["health_score"]+df["service_score"]+df["portion_score"])
print(df)

for x in range (0, len(data2)):
    currentRow = df.iloc[x]
    print(type(currentRow["taste_score"]))

#integer = df["taste_score"].int16(0).item()
#print (integer type)

#df["Average Score"] = df.iloc[[2,3]].mean(axis=1)
#print(df)
