# Configuracion de la DB


# db_config.py
import os
from google.cloud import firestore
from utils.credenciales import preparar_credenciales_google

# prepara credenciales al importar el módulo
preparar_credenciales_google()

# crea el cliente Firestore (usa el project de la env var si está)
_project = os.getenv("FIREBASE_PROJECT_ID")
db = firestore.Client(project=_project) if _project else firestore.Client()
