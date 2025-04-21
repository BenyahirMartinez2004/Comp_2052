from flask import Flask, render_template  # Importamos Flask para crear la aplicación y render_template para renderizar HTML.
from flask_wtf import FlaskForm  # Importamos FlaskForm para manejar formularios en Flask.
from wtforms import StringField, PasswordField, SubmitField  # Importamos los campos necesarios para el formulario.
from wtforms.validators import DataRequired, Email, Length  # Importamos validadores para verificar datos del formulario.

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"  # Configuramos una clave secreta para habilitar CSRF protection en Flask-WTF.

class RegisterForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(min=3)])  # Campo nombre, obligatorio y con longitud mínima.
    correo = StringField("Correo", validators=[DataRequired(), Email()])  # Campo correo, obligatorio y con formato válido.
    contraseña = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])  # Campo contraseña, obligatorio y con longitud mínima.
    submit = SubmitField("Registrarse")  # Botón de envío.

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()  # Instanciamos el formulario.
    if form.validate_on_submit():  # Validamos los datos del formulario.
        # Retornamos un mensaje indicando los datos del usuario registrado.
        return f"Usuario registrado: {form.nombre.data}, Correo: {form.correo.data}"
    # Renderizamos la página HTML del formulario con los datos actuales del formulario.
    return render_template('register.html', form=form)

# Verificamos si el archivo se ejecuta directamente.
if __name__ == "__main__":
    # Ejecutamos la aplicación en modo de depuración para facilitar el desarrollo.
    app.run(debug=True)