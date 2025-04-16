import firebase_admin
from firebase_admin import credentials, auth

# Caminho para o JSON de credenciais do Firebase
cred = credentials.Certificate("CAMINHO/para/seu/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
