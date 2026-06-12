import firebase_admin
from firebase_admin import credentials, firestore
from app.config.settings import settings

def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)

def get_firestore_client():
    initialize_firebase()
    return firestore.client()