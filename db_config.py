# db_config.py
import os
import tempfile
import firebase_admin
from firebase_admin import credentials, firestore


def preparar_credenciales_google():
    """Crea archivo temporal desde la env var GOOGLE_CREDENTIALS_JSON"""
    creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    if not creds_json:
        raise RuntimeError("Falta la variable de entorno GOOGLE_CREDENTIALS_JSON")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    tmp.write(creds_json.encode("utf-8"))
    tmp.flush()
    tmp.close()
    return tmp.name


# Crear el archivo temporal
cred_path = preparar_credenciales_google()

# Inicializar Firebase Admin con ese archivo
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Cliente Firestore listo para usar
db = firestore.client()
