from firebase.firebase_client import FirestoreBuffer

db = FirestoreBuffer().get_firestore()
doc_ref = db.collection(u'users').document(u'ace')
doc_ref.set({
    u'first': u'ahah',
    u'last': u'Lovelace',
    u'born': 186
})