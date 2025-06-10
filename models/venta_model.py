from database import db
#Definicion de la clase
class Venta(db.Model):
    __tablename__ = "ventas"
    #Definicion de los campos de la tabla
    id = db.Column(db.Integer,primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'),nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'),nullable=False)
    cantidad = db.Column(db.Integer,nullable=False)
    fecha = db.Column(db.DateTime,nullable=False)
    #Especificar relacion
    cliente = db.relationship('Cliente',back_populates='ventas')
    producto = db.relationship('Producto',back_populates='ventas')

    #Metodo constructor
    def __init__(self, cliente_id, producto_id, cantidad, fecha):
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha = fecha
    #Guarda en la base de datos, agrega la venta y guarda los cambios
    def save(self):
        db.session.add(self)
        db.session.commit()
    #Obtener todos las ventas, Devuelve los registros de la tabla ventas
    @staticmethod
    def get_all():
        return Venta.query.all()
    #Obtener una venta por id
    @staticmethod
    def get_by_id(id):
        return Venta.query.get(id)
    #Actualiza una venta, actualiza los campos
    def update(self, cliente_id=None, producto_id=None, cantidad=None, fecha=None):
        if cliente_id and producto_id and cantidad and fecha:
            self.cliente_id = cliente_id
            self.producto_id = producto_id
            self.cantidad = cantidad
            self.fecha = fecha
        db.session.commit()
    #Elimina la venta
    def delete(self):
        db.session.delete(self)
        db.session.commit()