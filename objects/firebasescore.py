from pyrebase import pyrebase

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

def get_username():
    pass