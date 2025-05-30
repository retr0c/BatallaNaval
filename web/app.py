import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Agrega la raíz del proyecto (BatallaNaval) al sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from BatallaNaval.src.Jugador import Jugador
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave-secreta-paila'

jugador = Jugador()

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/crear_cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        mensaje = jugador.crear_cuenta(usuario, contrasena)
        return render_template('crear_cuenta.html', mensaje=mensaje)
    return render_template('crear_cuenta.html')

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        resultado = jugador.iniciar_sesion(usuario, contrasena)
        if resultado == "Sesión iniciada":
            session['usuario'] = usuario
            return redirect(url_for('menu_principal'))
        return render_template('iniciar_sesion.html', mensaje=resultado)
    return render_template('iniciar_sesion.html')

@app.route('/menu_principal')
def menu_principal():
    if 'usuario' not in session:
        return redirect(url_for('menu'))
    return render_template('menu_principal.html', usuario=session['usuario'])

@app.route('/cerrar_sesion')
def cerrar_sesion():
    jugador.cerrar_sesion()
    session.pop('usuario', None)
    return redirect(url_for('menu'))

if __name__ == '__main__':
    app.run(debug=True)
