# Paso 1. Importar Flask, SocketIO y dotenv
import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Cargar las variables del archivo .env (datos sensibles fuera del código)
load_dotenv()

# Configuración de Firebase leída desde el .env
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
}

# Paso 2. Crear la aplicación y configurar SocketIO
app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*")


# Paso 3. Crear la ruta principal
@app.route("/")
def inicio():
    return render_template("login.html", firebase_config=firebase_config)

@app.route("/chat")
def chat():
    return render_template("index.html", firebase_config=firebase_config)


# Paso 4. Recibir mensajes desde los clientes
@socket.on("message")
def recibir_mensaje(mensaje):

    print("Mensaje recibido:", mensaje)

    # Enviar el mensaje a TODOS los usuarios conectados
    emit("mensaje", mensaje, broadcast=True)


# Paso 5. Inicializar el servidor
if __name__ == "__main__":

    # Aviso si falta algún dato de Firebase en el .env
    faltantes = [k for k, v in firebase_config.items() if not v]
    if faltantes:
        print("⚠️ Faltan datos de Firebase en el .env:", ", ".join(faltantes))

    socket.run(app, host="127.0.0.1",port=5000, debug=True)
