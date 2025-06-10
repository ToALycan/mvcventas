from database import db
#Definicion de la clase
class Producto(db.Model):
    __tablename__ = "productos"
    #Definicion de los campos de la tabla
    id = db.Column(db.Integer,primary_key=True)
    descripcion = db.Column(db.String(120),nullable=False)
    precio = db.Column(db.Float(11,2),nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    #Relacion con ventas
    ventas = db.relationship('Venta',back_populates='producto')
    #Metodo constructor
    def __init__(self, descripcion, precio, stock):
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    #Guarda en la base de datos, agrega el producto y guarda los cambios
    def save(self):
        db.session.add(self)
        db.session.commit()
    #Obtener todos los productos, Devuelve los registros de la tabla productos
    @staticmethod
    def get_all():
        return Producto.query.all()
    #Obtener un producto por id
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)
    #Actualiza un producto, actualiza los campos
    def update(self, descripcion=None, precio=None, stock=None):
        if descripcion and precio and stock:
            self.descripcion = descripcion
            self.precio = precio
            self.stock = stock
        db.session.commit()
    #Elimina el producto
    def delete(self):
        db.session.delete(self)
        db.session.commit()