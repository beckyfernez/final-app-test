

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope2 = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds2 = ServiceAccountCredentials.from_json_keyfile_name('gu-dining-locations-cf538c00daae.json', scope2)

client2 = gspread.authorize(creds2)

sheet = client2.open("Georgetown Dining Reviews Data").sheet1

data2 = sheet.get_all_records()

pprint(data2)

# storing dictionary values pulled from users in a list
#hard coded dictionary CHANGE LATER
sample_dict = {"location_id":"5", "taste_score":"2", "health_score":"2", "service_score":"2", "portion_score":"2", }
new_reviews = list(sample_dict.values())
integer_reviews = list(map(int, new_reviews))
#print(integer_reviews)

# writing new reviews onto the sheet (adapted from https://www.youtube.com/watch?v=T1vqS1NL89E)
sheet.insert_row(integer_reviews, 2)

#pprint(data2)