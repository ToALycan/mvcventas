from flask import render_template
def list(ventas):
    return render_template('venta/index.html', ventas = ventas)
def create(clientes, productos):
    # Se requiere productos y clientes
    return render_template('venta/create.html', clientes=clientes, productos=productos)
def edit(venta, clientes, productos):
    # Se requiere productos y clientes
    return render_template('venta/edit.html', venta = venta, clientes=clientes, productos=productos)