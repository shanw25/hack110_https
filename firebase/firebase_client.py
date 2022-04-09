import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreBuffer:
    db: any

    def __init__(self):
        # Use the application default credentials
        cred = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_firestore(self): 
        return self.db