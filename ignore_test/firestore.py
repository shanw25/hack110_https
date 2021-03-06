import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# firebase_admin.initialize_app(cred, {
#   'projectId': "585967269639",
# })

db = firestore.client()

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 186
})