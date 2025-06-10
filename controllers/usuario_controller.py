# Ruta	Qué hace	Método
# /usuarios/	Lista todos los usuarios	GET
# /usuarios/create	Muestra formulario o guarda nuevo usuario	GET / POST
# /usuarios/edit/<id>	Muestra o actualiza un usuario	GET / POST
# /usuarios/delete/<id>	Elimina un usuario	GET

# request: Permite acceder a datos enviados por formularios (como POST).
# redirect: Redirige a otra página.
# url_for: Genera URLs con nombre de funciones.
# Blueprint: Agrupa rutas en un módulo (útil para organizar código grande).
from flask import request, redirect, url_for, Blueprint
# Usuario: Modelo del usuario, conectado con la base de datos.
# usuario_view: Contiene las funciones para renderizar las plantillas HTML (list, create, edit).
from models.usuario_model import Usuario
from views import usuario_view
#Crea blueprint. Esto define un módulo de rutas. Todas las rutas aquí van a empezar con /usuarios.
usuario_bp = Blueprint('usuario',__name__,url_prefix="/usuarios")
# Ruta /usuarios/ – Ver todos los usuarios
# Se llama cuando entras a /usuarios/
# Recupera todos los usuarios con Usuario.get_all()
# Muestra la plantilla usando usuario_view.list(...)
@usuario_bp.route("/")
def index():
    #Recupera todos los registros de usuarios
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)
#  Ruta /usuarios/create – Crear nuevo usuario
# Si es GET: Muestra el formulario de creación (create.html)
# Si es POST: Recoge los datos del formulario, crea un usuario y lo guarda.
# Luego redirige a la lista de usuarios (usuario.index)
@usuario_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        usuario = Usuario(nombre,username,password,rol)
        usuario.save()
        return redirect(url_for('usuario.index'))
    return usuario_view.create()
# Ruta /usuarios/edit/<id> – Editar un usuario
# GET: Muestra el formulario con los datos del usuario actual.
# POST: Actualiza los datos con los del formulario.
# Redirige a la lista de usuarios después de guardar.
@usuario_bp.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']
        #Actualizar
        usuario.update(nombre=nombre,username=username,password=password,rol=rol)
        return redirect(url_for('usuario.index'))
    return usuario_view.edit(usuario)
#  Ruta /usuarios/delete/<id> – Eliminar usuario
# Busca al usuario por su ID.
# Lo elimina de la base de datos.
# Redirige a la lista de usuarios.
@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))