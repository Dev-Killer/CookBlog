from json import load
from os import getenv
import pyrebase
from cookApp.settings import DEBUG

CONFIG = dict()
if(int(DEBUG)):
    with open("firebase.json", "r") as f:
        CONFIG = load(f)
        print(CONFIG)

else:
    CONFIG = {
        "apiKey":  getenv("API_KEY_FIREBASE"),
        "authDomain": getenv("AUTH_DOMAIN"),
        "projectId": getenv("PROJECT_ID"),
        "storageBucket": getenv("STORAGE_BUCKET"),
        "messagingSenderId": getenv("MESSAGING_SENDER_ID"),
        "appId": getenv("APP_ID"),
        "measurementId": getenv("MEASUREMENT_ID"),
        "databaseURL":"test",
    }


    
firebase = pyrebase.initialize_app(CONFIG)

storage = firebase.storage()
database = firebase.database()
