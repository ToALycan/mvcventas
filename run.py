# Flask: clase principal para crear la aplicación web.
# request: para obtener la URL actual del navegador.
# controllers: se importan los controladores de cada módulo.
# db: objeto SQLAlchemy para manejar la base de datos.
from flask import Flask,request, render_template
from controllers import usuario_controller, cliente_controller, producto_controller, venta_controller
from database import db
# Se crea la aplicación Flask, Esto inicia la app web.
app = Flask(__name__)
# Configuración de base de datos:
# Usa SQLite como motor de base de datos (ventas.db).
# Desactiva el rastreo de cambios en SQLAlchemy para mejorar el rendimiento.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Se vincula la base de datos con la app Flask:
# Esto le dice a SQLAlchemy que use esta instancia de Flask para conectarse y trabajar.
db.init_app(app)
# Registra los blueprints:
# Un blueprint es una forma de modularizar rutas. Aquí se añaden los controladores separados para:
# Usuario, Cliente, Producto, Venta
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(venta_controller.venta_bp)
# Función para activar menús en la navegación:
# Esta función permite usar en los templates algo como:
# <li class="{{ is_active('/clientes') }}">Clientes</li>
# Así puedes resaltar el menú actual con Bootstrap (clase active), según la URL.
@app.context_processor
def injec_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return(dict(is_active = is_active))
# Ruta principal:
# Cuando entras a http://localhost:5000/, verás el texto "Aplicacion ventas". Es solo una prueba sencilla.
@app.route("/")
def home():
    return render_template('usuario/index.html')
# Ejecutar la aplicación:
# with app.app_context(): db.create_all(): crea las tablas en la base de datos si no existen.
# app.run(debug=True): lanza la app en modo debug, útil para desarrollo (recarga automática y muestra errores).
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)