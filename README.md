# final-app-test


#also include information on how to create credentials on google cloud console, obtain keys, download json, and share google sheets with client email (this is only a one time thing for each workbook)


#set up credentials
#share google sheets with client email

#.env file
#set up google_sheet_id environmental variable

#Setup
```sh
pip install -r requirements.txt
```

#Read csv file from "inputs" google sheets
```sh
python locations.py
```


#create app directory and include locations.py and review_submit.py and reviewaggregation.py
#this is since these code files should run seperate from the web application


#Heroku setup
#heroku configure env. variable


#add heroku buildpack to create the json file from the local environment
#manually config json file on heroku
#copy contents from json file
#git push heroku main


#testing
#pytest


