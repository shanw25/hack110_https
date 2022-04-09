import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_firebase_admin():
    # Use the application default credentials
    cred = credentials.Certificate("../serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()
