import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from BatallaNaval.src.Jugador import Jugador
from BatallaNaval.src.Juego import Juego
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave-secreta-paila'

jugador = Jugador()
juego = Juego()

# Función para mostrar el campo como string
def renderizar_campo(campo):
    campo_str = ""
    for fila in campo:
        for celda in fila:
            campo_str += " X " if celda == "X" else " ~ "
        campo_str += "\n"
    return campo_str

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

@app.route('/cambiar_contrasena', methods=['POST'])
def cambiar_contrasena():
    nueva_contrasena = request.form.get('nueva_contrasena')

    # Validar que haya usuario activo en sesión
    usuario_actual = session.get('usuario')
    contrasena_actual = session.get('contrasena')

    if not usuario_actual:
        return "No hay sesión activa", 401
    
    jugador = Jugador(nombre=usuario_actual, contrasena=contrasena_actual)
    resultado = jugador.cambiar_contraseña(nueva_contrasena)

    if resultado == "Contraseña cambiada exitosamente":
        # Actualizamos la contraseña en la sesión
        session['contrasena'] = nueva_contrasena
        return redirect(url_for('menu'))  # o a donde quieras redirigir
    else:
        # En caso de error, devuelves el mensaje (o podrías mostrar en plantilla)
        return resultado, 400
    
@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    if 'usuario' not in session:
        return redirect(url_for('menu'))

    mensaje = error = None

    if request.method == 'POST':
        if 'ancho' in request.form:
            try:
                ancho = int(request.form['ancho'])
                alto = int(request.form['alto'])
                naves = int(request.form['naves'])

                campo = juego.iniciar_campo_juego(ancho, alto, naves)
                session['campo'] = campo
                session['score'] = 0
                mensaje = "¡Juego iniciado!"
            except ValueError:
                error = "Parámetros inválidos."
        elif 'fila' in request.form:
            try:
                fila = int(request.form['fila']) - 1
                columna = int(request.form['columna']) - 1
                campo = session.get('campo')
                score = session.get('score', 0)

                resultado = juego.disparar(campo, fila, columna)

                if resultado == "¡Impacto!":
                    score += 10
                elif resultado == "Agua":
                    score -= 2

                session['score'] = score
                session['campo'] = campo

                if not any(1 in fila for fila in campo):
                    mensaje = f"¡Ganaste! Puntaje final: {score}"
                    session.pop('campo', None)
                else:
                    mensaje = f"{resultado}. Puntaje actual: {score}"
            except Exception as e:
                error = f"Error al disparar: {str(e)}"

    campo = session.get('campo')
    score = session.get('score', 0)
    campo_str = renderizar_campo(campo) if campo else None

    return render_template('juego.html',
                           usuario=session['usuario'],
                           campo=campo,
                           campo_str=campo_str,
                           score=score,
                           mensaje=mensaje,
                           error=error)

@app.route('/disparar', methods=['POST'])
def disparar():
    return jugar()

if __name__ == '__main__':
    app.run(debug=True)
