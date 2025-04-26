from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Base de datos simulada con contraseñas almacenadas como hash y roles asignados
usuarios = {
    'admin': {'password': generate_password_hash('12345'), 'role': 'admin'},
    'bmartinez': {'password': generate_password_hash('Goji#1124'), 'role': 'user'}
}

# Clase de Usuario
class Usuario(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

# Cargar usuario desde la sesión
@login_manager.user_loader
def load_user(user_id):
    # Verifica que el usuario exista y, de ser así, obtiene el rol
    user_data = usuarios.get(user_id)
    if user_data:
        return Usuario(user_id, user_data['role'])
    return None

# Ruta principal protegida
@app.route('/')
@login_required
def home():
    return render_template('login.html.jinja2') #,nombre=current_user.id

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']  # Procesar usuario enviado
        password = request.form['password']  # Procesar password enviado

        # Validar si los datos enviados existen y verificar el hash de la contraseña
        if username in usuarios and check_password_hash(usuarios[username]['password'], password):
            user = Usuario(username, usuarios[username]['role'])
            login_user(user)
            # Redirigir según el rol del usuario
            if user.role == 'admin':
                return redirect(url_for('admin_panel'))
            elif user.role == 'user':
                return redirect(url_for('user_panel'))
        
        return render_template("error.html.jinja2", error_code=401, 
                               error_message="Credenciales Invalidas (error con el username o password)!"), 401
    return render_template('login.html.jinja2')

# Panel del administrador
@app.route('/admin')
@login_required
def admin_panel():
    if current_user.role != 'admin':
        return "Acceso denegado", 403
    return render_template('admin.html.jinja2', nombre=current_user.id)

# Panel del usuario
@app.route('/user')
@login_required
def user_panel():
    return render_template('user.html.jinja2', nombre=current_user.id)

# Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)