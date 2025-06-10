from database import db
from werkzeug.security import generate_password_hash, check_password_hash

# Este código te permite manejar una tabla de usuarios como si fuera un objeto de Python. Así puedes:
# Crear un usuario: u = Usuario("Ana", "ana12", "secreta", "admin")
# Guardarlo: u.save()
# Consultarlo por ID: Usuario.get_by_id(1)
# Verificar la contraseña: u.verify_password("secreta")

#Definicion de la clase
class Usuario(db.Model):
    __tablename__ = "usuarios"
    #Definicion de los campos de la tabla
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String,nullable=False)
    rol = db.Column(db.String(20),nullable=False)
    #Metodo constructor
    def __init__(self, nombre, username, password, rol):
        self.nombre = nombre
        self.username = username
        self.password = self.hash_password(password)
        self.rol = rol
    #Encriptacion de contraseñas
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    #Verificaion de contraseña
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    #Guarda en la base de datos, agrega el usuario y guarda los cambios
    def save(self):
        db.session.add(self)
        db.session.commit()
    #Obtener todos los usuarios, Devuelve los registros de la tabla usuarios
    @staticmethod
    def get_all():
        return Usuario.query.all()
    #Obtener un usuario por id
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    #Actualiza un usuario, actualiza los campos y tambien encripta la la contraseña si se pasan nuevos valores
    def update(self, nombre=None, username=None, password=None, rol=None):
        if nombre:
            self.nombre = nombre
        if username:
            self.username = username
        if password:
            self.password = self.hash_password(password)
        if rol:
            self.rol = rol
        db.session.commit()
    #Elimina el usuario
    def delete(self):
        db.session.delete(self)
        db.session.commit()