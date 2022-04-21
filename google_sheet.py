# source code : https://www.youtube.com/watch?v=gkglr8GID5E

import os
from Google import Create_Service
#import pandas

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "sheets"
API_VERSION = "v4"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
spreadsheet_id = "1ciNHuyNCIMAYaBFQDNCykwwdWVEZwr2Uo8TnkHcO2Qg"

# Get method - single cell range of values
response = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    majorDimension="ROW",
    range='dining_locations!A1:B15'
).execute()

print(response)