# utils/credenciales.py
import os, tempfile


def preparar_credenciales_google():
    """Crea un archivo temporal con el JSON de credenciales y
    exporta GOOGLE_APPLICATION_CREDENTIALS al path generado."""
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

    creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    if not creds_json:
        print("ADVERTENCIA: falta GOOGLE_CREDENTIALS_JSON")
        return None

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    tmp.write(creds_json.encode("utf-8"))
    tmp.flush()
    tmp.close()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = tmp.name
    return tmp.name
