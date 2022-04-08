from asyncio import constants
from pyrebase import pyrebase
from constants import WIN
config = {
    "apiKey": "AIzaSyDCE-OZxIDIWvZ2-adM5xHRii8iZzAsVvE",
    "authDomain": "aipygamescore.firebaseapp.com",
    "projectId": "aipygamescore",
    "databaseURL": "https://aipygamescore-default-rtdb.firebaseio.com/",
    "storageBucket": "aipygamescore.appspot.com",
    "messagingSenderId": "36142704262",
    "appId": "1:36142704262:web:046e5408ebbcafde8c1307",
    "measurementId": "G-B67NE6N4B6"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

def senddata(username, score):
    data = {"Username": username,"score": score}
    database.child("All scores").push(data)
    v = database.child("HighScore").get()
    value = (v.val().get("score"))
    if (score > value):
        database.child("HighScore").set(data)