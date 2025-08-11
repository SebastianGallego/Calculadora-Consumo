import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
from datetime import datetime
import json
import os
import requests
from db_config import db
from session import session


CLIENT_SECRET_FILE = "google_oauth.json"
TOKEN_FILE = "token.json"
SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]


# === Login Automático con token persistente ===
def login_google_automatico():
    creds = None

    # 1. Intentamos cargar credenciales guardadas
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as token:
            creds_data = json.load(token)

        # Verificamos que tenga refresh_token
        if "refresh_token" not in creds_data:
            print("❌ Token sin refresh_token. Borrando archivo...")
            os.remove(TOKEN_FILE)
            creds_data = None
        else:
            creds = google.oauth2.credentials.Credentials.from_authorized_user_info(
                creds_data, SCOPES
            )

    # 2. Si están vencidas pero se pueden renovar
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
        except Exception as e:
            print("Error al refrescar token:", e)
            creds = None

    # 3. Si no hay credenciales válidas, iniciar login
    if not creds or not creds.valid:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES
        )
        creds = flow.run_local_server(port=8080)

        # Solo si contiene refresh_token, guardamos
        if creds.refresh_token:
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())
        else:
            print(
                "⚠️ Login exitoso, pero no se recibió refresh_token. No se guardará token.json."
            )

    # 4. Obtener info del usuario
    headers = {"Authorization": f"Bearer {creds.token}"}
    response = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo", headers=headers
    )

    if response.status_code == 200:
        user_info = response.json()
        ip_info = requests.get("https://ipinfo.io").json()
        pais = ip_info.get("country", "Desconocido")
        ciudad = ip_info.get("city", "Desconocido")
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Guardar login en Firestore
        login_ref = db.collection("estadisticas").document()
        login_ref.set(
            {
                "fecha_hora": fecha_actual,
                "pais": pais,
                "ciudad": ciudad,
                "email": user_info["email"],
            }
        )

        print(
            f"\n✅ Usuario autenticado: {user_info['email']} - {pais}, {ciudad} - {fecha_actual}"
        )
        return user_info

    else:
        print("❌ Error al obtener la información del usuario")
        return None

    # Guardamos en sesión para usarlo en toda la app
    session.usuario = {"email": user_info["email"], "pais": pais, "ciudad": ciudad}
