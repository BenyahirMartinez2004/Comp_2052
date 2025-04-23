from flask import Flask
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, AnonymousIdentity

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"  # Configuración de una clave secreta para seguridad.

# Configuración de Flask-Principal
Principal(app)

# Crear permisos basados en roles
admin_permission = Permission(RoleNeed('admin'))  # Permiso para administradores.
user_permission = Permission(RoleNeed('user'))  # Permiso para usuarios regulares.
edit_permission = Permission(RoleNeed('edit'))  # Permiso para editores.

# Simular un usuario con roles (modificar según necesidad)
current_user = {"role": "edit"}  # Cambiar el rol para probar permisos distintos.

# Configuración dinámica de identidad basada en el rol del usuario
@app.before_request
def set_identity():
    if current_user["role"] == "admin":
        identity_changed.send(app, identity=Identity('admin'))
    elif current_user["role"] == "user":
        identity_changed.send(app, identity=Identity('user'))
    elif current_user["role"] == "edit":
        identity_changed.send(app, identity=Identity('edit'))
    else:
        identity_changed.send(app, identity=AnonymousIdentity())

# Ruta principal accesible para todos
@app.route('/')
def index():
    return "Bienvenido a la Página Principal"

# Ruta protegida para administradores
@app.route('/admin')
def admin():
    if current_user["role"] == "admin":
        return "Panel de Administrador: Acceso permitido para administradores"
    else:
        return "Acceso Denegado: No tienes los permisos necesarios", 403

# Ruta protegida para usuarios regulares
@app.route('/user')
def user():
    if current_user["role"] == "user":
        return "Panel de Usuario: Acceso permitido para usuarios regulares"
    else:
        return "Acceso Denegado: No tienes los permisos necesarios", 403

# Ruta protegida para editores
@app.route('/edit')
def edit():
    if current_user["role"] == "edit":
        return "Página de Edición: Acceso permitido"
    else:
        return "Acceso Denegado: No tienes los permisos necesarios", 403

# Verificación para ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)