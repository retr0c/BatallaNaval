# Batalla Naval
Proyecto de juego Batalla Naval con pruebas unitarias.

Este proyecto es una implementación del clásico juego Batalla Naval, desarrollado en Python, que incluye tres formas de interacción:

Interfaz por consola: Para jugar desde la terminal con menús y comandos simples.

Interfaz gráfica: Usando Kivy para una experiencia visual más amigable.

Interfaz web: Basada en Flask, para jugar desde el navegador con funcionalidades completas de usuario (registro, inicio de sesión, cambio de contraseña, juego, etc).

Además, el proyecto cuenta con:

Persistencia de datos usando una base de datos PostgreSQL para guardar usuarios y partidas.

Pruebas unitarias para asegurar el correcto funcionamiento de la lógica.

Organización modular del código con separación de lógica, interfaz y base de datos.



Pruebas Unitarias - Proyecto Batalla Naval

Este documento presenta las pruebas unitarias realizadas para las funcionalidades principales del proyecto Batalla Naval.

Estructura de las Pruebas

Las pruebas están organizadas en el directorio tests y se dividen por funcionalidad.

Pruebas realizadas

1. test_iniciar_sesion

Descripción: Pruebas para verificar el proceso de inicio de sesión.

Ubicación: tests/test_iniciar_sesion.py

![Tabla de pruebas:](ProyectoBatallaNaval/Test-iniciar-sesion.png)


2. test_campo_juego

Descripción: Pruebas para la correcta inicialización del campo de juego.

Ubicación: tests/test_campo_juego.py

![Tabla de pruebas:](ProyectoBatallaNaval/Test_iniciar-campo-de-juego.png)



3. test_crear_cuenta

Descripción: Pruebas para el proceso de creación de una nueva cuenta.

Ubicación: tests/test_crear_cuenta.py

![Tabla de pruebas:](ProyectoBatallaNaval/Test-crear-cuenta.png)



4. test_disparar

Descripción: Pruebas para verificar la acción de disparar en el juego.

Ubicación: tests/test_disparar.py

![Tabla de pruebas:](ProyectoBatallaNaval/Test-Disparar.png)



5. test_cambiar_contrasena

Descripción: Pruebas para verificar el proceso de cambio de contraseña.

Ubicación: tests/test_cambiar_contrasena.py

![Tabla de pruebas:](ProyectoBatallaNaval/Test-cambiar-contraseña.png)

6. test_puntuacion

Descripción: Pruebas para verificar el sistema de puntuación del juego.

Ubicación: tests/test_puntuacion.py

![Tabla de pruebas:](ProyectoBatallaNaval/Test-visualizar-puntacion.png)



Diagrama de clases:

![Diagrama de clases:](ProyectoBatallaNaval/DiagramadeClases.png)

instalar los requerimientos:
pip install -r requirements.txt

⚠️ Antes de ejecutar setup_db.py, asegúrate de tener PostgreSQL instalado, corriendo en el sistema y cambiar la contraseña del superusuario en el archivo setup_db.py si no es "postgres".
        
Configurar todo:
python setup_db.py


Para ejecutar las pruebas:
python -m unittest discover -s tests -p "*.py" -v


Para ejecutar el programa:

python menu_consola.py
python menu_grafico.py

# Ejecutar la versión web
cd web
python app_web.py
Pegar en el navegador la url proporcionada


