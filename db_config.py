# Configuracion de la DB


import firebase_admin
from firebase_admin import credentials, firestore
from config import RUTA

# === Configuración Firebase y Google OAuth ===
cred = credentials.Certificate(RUTA)
firebase_admin.initialize_app(cred)
db = firestore.client()

