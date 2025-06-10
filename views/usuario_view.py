from flask import render_template
#Muestra todos los usuarios
# Muestra la página usuarios/index.html.
# Le pasa una variable llamada usuarios (probablemente una lista de usuarios desde la base de datos).
# Esa variable se puede usar en el HTML con Jinja, por ejemplo:
# {% for u in usuarios %}
#   <p>{{ u.nombre }}</p>
# {% endfor %}
def list(usuarios):
    return render_template('usuario/index.html', usuarios = usuarios)
#Muestra formulario vacio para crear usuario
# Muestra la plantilla usuario/create.html.
# Generalmente contiene un formulario para crear un nuevo usuario.
# No recibe datos porque solo muestra el formulario vacío.
def create():
    return render_template('usuario/create.html')
#Muestra formulario lleno para editar usuario
# Muestra la plantilla usuario/edit.html.
# Le pasa la variable usuario, que contiene los datos del usuario a editar.
# En la plantilla puedes rellenar un formulario con esos datos, como:
# <input type="text" name="nombre" value="{{ usuario.nombre }}">
def edit(usuario):
    return render_template('usuario/edit.html', usuario = usuario)