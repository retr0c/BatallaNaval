from BatallaNaval.src.Jugador import Jugador
from BatallaNaval.src.Juego import Juego
import sys

from BatallaNaval.src.Puntuacion import Puntuacion

def mostrar_campo(campo, revelar=False):
    for fila in campo:
        linea = ""
        for celda in fila:
            if celda == "X":
                linea += " X "
            elif celda == 1:
                linea += " ~ " if not revelar else " 1 "
            else:
                linea += " ~ "
        print(linea)
    print()  

def mostrar_menu():
    print("\n🚢 ¡Bienvenido a Batalla Naval! 🚢")
    print("1️⃣ Crear cuenta")
    print("2️⃣ Iniciar sesión")
    print("3️⃣ Salir")

def menu_principal(jugador):
    while True:
        print("\n🎮 Menú Principal 🎮")
        print("1️⃣ Jugar")
        print("2️⃣ Cambiar contraseña")
        print("3️⃣ Cerrar sesión")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar(jugador)
        elif opcion == "2":
            nueva_contraseña = input("Nueva contraseña: ")
            print(jugador.cambiar_contraseña(nueva_contraseña))
        elif opcion == "3":
            cerrar_sesion(jugador)
            print("Cerrando sesión...")
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")
            

def cerrar_sesion(jugador):
    global puntuaciones_jugadores  

    if jugador.usuario_actual in puntuaciones_jugadores:
        puntuaciones_jugadores[jugador.usuario_actual] = 0  
    
    print(f"👋 {jugador.usuario_actual}, has cerrado sesión. Tu puntuación ha sido reiniciada.")
    jugador.cerrar_sesion()  
            

puntuaciones_jugadores = {}

def jugar(jugador):
    global puntuaciones_jugadores  
    
    juego = Juego()
    
    
    if jugador not in puntuaciones_jugadores:
        puntuaciones_jugadores[jugador] = 0  

    try:
        ancho = int(input("Ingrese el ancho del campo de juego: "))
        alto = int(input("Ingrese el alto del campo de juego: "))
        naves = int(input("Ingrese el número de naves a colocar: "))
        campo = juego.iniciar_campo_juego(ancho, alto, naves)
    except ValueError:
        print("❌ Error: Ingresa solo números enteros.")
        return

    print("\n🛳 Campo de batalla generado. ¡Comienza el juego!")

    while True:
        print("Estado actual del campo:")
        mostrar_campo(campo)
        try:
            fila = int(input("Elige la fila: ")) - 1
            columna = int(input("Elige la columna: ")) - 1
        except ValueError:
            print("❌ Ingresa números válidos para la fila y columna.")
            continue

        try:
            resultado = juego.disparar(campo, fila, columna)
            if resultado == "¡Impacto!":
                puntuaciones_jugadores[jugador] += 10  
            elif resultado == "Agua":
                puntuaciones_jugadores[jugador] -= 2  

            print(f"🎯 Resultado: {resultado}")
            print(f"⭐ Puntuación actual: {puntuaciones_jugadores[jugador]}")
        except IndexError:
            print("❌ Coordenadas fuera de rango, intenta de nuevo.")
            continue

        if all(all(celda != 1 for celda in fila) for fila in campo):
            print("\n🎉 ¡Has hundido todas las naves! 🎉")
            print("Campo final:")
            mostrar_campo(campo, revelar=True)
            break

        seguir = input("¿Deseas seguir disparando? (s/n): ").lower()
        if seguir != 's':
            print(f"📊 Puntuación final: {puntuaciones_jugadores[jugador]}")
            print("Saliendo del juego...")
            break




def main():
    jugador = Jugador()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            print(jugador.crear_cuenta(usuario, contraseña))
        elif opcion == "2":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            resultado = jugador.iniciar_sesion(usuario, contraseña)
            print(resultado)
            if resultado == "Sesión iniciada":
                menu_principal(jugador)
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
