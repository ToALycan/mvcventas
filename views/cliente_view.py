from flask import render_template
def list(clientes):
    return render_template('cliente/index.html', clientes = clientes)
def create():
    return render_template('cliente/create.html')
def edit(cliente):
    return render_template('cliente/edit.html', cliente = cliente)