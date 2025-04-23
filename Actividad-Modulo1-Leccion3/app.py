from flask import Flask, jsonify, request  # Importamos Flask, jsonify y request para crear la aplicación y manejar solicitudes HTTP.

# Creamos una instancia de Flask.
app = Flask(__name__)

# Listas en memoria para almacenar datos de usuarios y productos.
usuarios = []
productos = []

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({"mensaje": "Sistema de gestion de productos y usuarios"})

# Ruta POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():

    data = request.json  # Obtenemos el cuerpo de la solicitud en formato JSON.
    nombre = data.get("nombre")  # Nombre del usuario.
    correo = data.get("correo")  # Correo del usuario.
    Id = data.get("Id")  # Id del usuario (opcional).

    if not nombre or not correo:  # Validamos que 'nombre' y 'correo' existan.
        return jsonify({"error": "Nombre y correo son obligatorios"}), 400

    # Creamos el nuevo usuario.
    usuario = {"Id": Id, "nombre": nombre, "correo": correo}
    usuarios.append(usuario)  # Agregamos el usuario a la lista.
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": usuario})

# Ruta GET /usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

# Ruta POST /crear_producto
@app.route("/crear_producto", methods=["POST"])
def crear_producto():
    data = request.json  # Obtenemos el cuerpo de la solicitud en formato JSON.
    Idproducto = data.get("Idproducto")  # Id del producto.
    nombre = data.get("nombre")  # Nombre del producto.
    precio = data.get("precio")  # Precio del producto.
    disponible = data.get("disponible", True)  # Disponibilidad del producto (por defecto True).

    if not nombre or not precio:  # Validamos que 'nombre' y 'precio' existan.
        return jsonify({"error": "Nombre y precio son obligatorios"}), 400

    # Creamos el nuevo producto.
    producto = {"Idproducto": Idproducto, "nombre": nombre, "precio": precio, "disponible": disponible}
    productos.append(producto)  # Agregamos el producto a la lista.
    return jsonify({"mensaje": "Producto creado exitosamente", "producto": producto})

# Ruta GET /productos
@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify({"productos": productos})

# Verificamos si el script se está ejecutando directamente.
if __name__ == "__main__":
    # Ejecutamos la aplicación en modo de depuración.
    app.run(debug=True)