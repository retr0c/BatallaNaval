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

def renderizar_campo(campo):
    """
    Convierte la matriz del campo de juego en una cadena legible
    con 'X' para impactos y '~' para agua.

    Args:
        campo (list): Matriz del campo de juego.

    Returns:
        str: Representación visual del campo.
    """
    campo_str = ""
    for fila in campo:
        for celda in fila:
            campo_str += " X " if celda == "X" else " ~ "
        campo_str += "\n"
    return campo_str

@app.route('/')
def menu():
    """
    Ruta inicial. Muestra el menú principal con opciones.

    Returns:
        Render: Plantilla del menú.
    """
    return render_template('menu.html')

@app.route('/crear_cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    """
    Permite al usuario crear una cuenta nueva. 
    Maneja tanto el formulario como la respuesta.

    Returns:
        Render: Página con formulario o resultado.
    """
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        mensaje = jugador.crear_cuenta(usuario, contrasena)
        return render_template('crear_cuenta.html', mensaje=mensaje)
    return render_template('crear_cuenta.html')

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    """
    Permite al usuario iniciar sesión. Verifica credenciales.

    Returns:
        Redirect o Render: Redirige al menú principal o muestra mensaje.
    """
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
    """
    Muestra el menú principal del juego si hay sesión activa.

    Returns:
        Render o Redirect: Página principal o redirección si no hay sesión.
    """
    if 'usuario' not in session:
        return redirect(url_for('menu'))
    return render_template('menu_principal.html', usuario=session['usuario'])

@app.route('/cerrar_sesion')
def cerrar_sesion():
    """
    Cierra la sesión del usuario y lo redirige al menú principal.

    Returns:
        Redirect: Redirección al menú principal.
    """
    jugador.cerrar_sesion()
    session.pop('usuario', None)
    return redirect(url_for('menu'))

@app.route('/cambiar_contrasena', methods=['POST'])
def cambiar_contrasena():
    """
    Permite al usuario cambiar su contraseña si tiene sesión activa.

    Returns:
        Redirect o str: Redirección si éxito, error en caso contrario.
    """
    nueva_contrasena = request.form.get('nueva_contrasena')
    usuario_actual = session.get('usuario')
    contrasena_actual = session.get('contrasena')

    if not usuario_actual:
        return "No hay sesión activa", 401
    
    jugador = Jugador(nombre=usuario_actual, contrasena=contrasena_actual)
    resultado = jugador.cambiar_contraseña(nueva_contrasena)

    if resultado == "Contraseña cambiada exitosamente":
        session['contrasena'] = nueva_contrasena
        return redirect(url_for('menu'))
    else:
        return resultado, 400

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    """
    Lógica principal del juego. Permite configurar el campo y disparar.

    Returns:
        Render: Página del juego con el campo, puntaje y mensajes.
    """
    if 'usuario' not in session:
        return redirect(url_for('menu'))

    mensaje = error = None

    if request.method == 'POST':
        if 'ancho' in request.form:
            # Inicializar campo
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
            # Disparar en el campo
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
    """
    Ruta secundaria que redirige a la lógica de disparar en el juego.

    Returns:
        Response: Llama la función jugar().
    """
    return jugar()

if __name__ == '__main__':
    app.run(debug=True)
