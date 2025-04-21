from flask import Flask, render_template, jsonify, request  # Importamos las herramientas necesarias para crear nuestra aplicación.

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    data = {"title": "Inicio", "message": "Bienvenidos a TechNova"}
    return render_template('index.html', data=data)

# Ruta para la página de contacto
@app.route('/contacto')
def about():
    data = {"title": "Contactanos", "message": "¿Tienes alguna duda, consulta sobre un producto o necesitas asistencia?"}
    return render_template('contacto.html', data=data)

# Ruta para mostrar los productos
@app.route('/productos')
def productos():
    data = {
        "title": "Inventario de Productos",
        "productos": [
            {"nombre": "Laptop", "precio": 1200, "disponible": True},
            {"nombre": "Smartphone", "precio": 800, "disponible": False},
            {"nombre": "Tablet", "precio": 300, "disponible": True}
        ]
    }
    return render_template('productos.html', data=data)

# Base de datos simulada en memoria
sugerencias = {
    "sugerencias": []
}

# Ruta para ver sugerencias (vista HTML)
@app.route('/sugerencias', methods=["GET"])
def sugerencia():
    return render_template("sugerencias.html", data=sugerencias)

# Ruta para obtener sugerencias en formato JSON
@app.route('/sugerencias')
def escojer_sugerecias():
    return jsonify(sugerencias)

# Ruta para agregar una nueva sugerencia
@app.route("/sugerecia", methods=["POST"])
def crear_sugerecias():
    data = request.json
    objeto_sugerencia = data.get('sugerecia')
    if not objeto_sugerencia:
        return jsonify({"error": "Datos incompletos"}), 400
    
    sugerencias["sugerencias"].append(objeto_sugerencia)
    return jsonify({"message": "Nueva sugerencia creada"}), 201

# Ruta para eliminar sugerencias
@app.route("/sugerecias", methods=["DELETE"])
def borrar_sugerecias():
    data = request.json
    objecto_sugerencia = data.get('sugerencia')
    if not objecto_sugerencia:
        return jsonify({"error": "Datos incompletos"}), 400
    
    if objecto_sugerencia not in sugerencias["sugerencias"]:
        return jsonify({"error": "Sugerencia no encontrada"}), 404

    sugerencias["sugerencias"].remove(objecto_sugerencia)
    return jsonify({"message": f"Sugerencia '{objecto_sugerencia}' eliminada"}), 200

# Ruta para actualizar una sugerencia
@app.route("/sugerencias", methods=["PUT"])
def update_todo():
    data = request.json
    old_sugerencia = data.get('old')
    new_sugerencia = data.get('new')

    if not old_sugerencia or not new_sugerencia:
        return jsonify({"error": "Datos incompletos"}), 400

    if old_sugerencia not in sugerencias["sugerencias"]:
        return jsonify({"error": "Sugerencia no encontrada"}), 404

    index = sugerencias["sugerencias"].index(old_sugerencia)
    sugerencias["sugerencias"][index] = new_sugerencia

    return jsonify({"message": f"Sugerencia actualizada de '{old_sugerencia}' a '{new_sugerencia}'"}), 200

# Verificar si el archivo se ejecuta directamente
if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)