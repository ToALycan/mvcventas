from database import db
#Definicion de la clase
class Cliente(db.Model):
    __tablename__ = "clientes"
    #Definicion de los campos de la tabla
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    telefono = db.Column(db.String(20),nullable=False)
    #Relacion con ventas
    ventas = db.relationship('Venta',back_populates='cliente')
    #Metodo constructor
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    #Guarda en la base de datos, agrega el cliente y guarda los cambios
    def save(self):
        db.session.add(self)
        db.session.commit()
    #Obtener todos los clientes, Devuelve los registros de la tabla clientes
    @staticmethod
    def get_all():
        return Cliente.query.all()
    #Obtener un cliente por id
    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)
    #Actualiza un cliente, actualiza los campos y tambien encripta la la contraseña si se pasan nuevos valores
    def update(self, nombre=None, email=None, telefono=None):
        if nombre and email and telefono:
            self.nombre = nombre
            self.email = email
            self.rol = telefono
        db.session.commit()
    #Elimina el cliente
    def delete(self):
        db.session.delete(self)
        db.session.commit()