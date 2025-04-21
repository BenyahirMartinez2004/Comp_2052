from flask import Flask, request  # Importa la clase Flask y el módulo request

# Crea una instancia de Flask para la aplicación web
app = Flask(__name__)

# Define una ruta para el endpoint "/info" que solo permite solicitudes GET
@app.route("/info", methods=["GET"])
def info():
    return {"message": "Una API de ejemplo usando Flask"}

# Define una ruta para el endpoint "/mensaje" que solo permite solicitudes POST
@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json  # Obtiene el cuerpo de la solicitud en formato JSON
    mensaje = data.get("mensaje", "Sin mensaje")  # Extrae el mensaje o usa un valor predeterminado
    return {"respuesta": f"Recibido: {mensaje}"}

# Verifica si el script se ejecuta directamente y levanta el servidor de desarrollo
if __name__ == "__main__":
    # Ejecuta la aplicación en modo de depuración para facilitar el desarrollo
    app.run(debug=True)