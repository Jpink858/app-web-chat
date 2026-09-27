# Paso 1. Importar Flask y SocketIO
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Paso 2. Crear la aplicación y configurar SocketIO
app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*")


# Paso 3. Crear la ruta principal
@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/chat")
def chat():
    return render_template("index.html")


# Paso 4. Recibir mensajes desde los clientes
@socket.on("message")
def recibir_mensaje(mensaje):

    print("Mensaje recibido:", mensaje)

    # Enviar el mensaje a TODOS los usuarios conectados
    emit("mensaje", mensaje, broadcast=True)


# Paso 5. Inicializar el servidor
if __name__ == "__main__":
    socket.run(app, host="127.0.0.1",port=5000, debug=True)