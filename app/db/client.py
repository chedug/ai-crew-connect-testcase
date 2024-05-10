import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

PATH_TO_SERVICE_ACCOUNT_KEY = os.getenv("PATH_TO_SERVICE_ACCOUNT_KEY")

cred = credentials.Certificate(PATH_TO_SERVICE_ACCOUNT_KEY)
firebase_admin.initialize_app(cred)

db = firestore.client()
