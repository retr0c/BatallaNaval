from BatallaNaval.base_datos.db import crear_usuario, obtener_usuario,  actualizar_contrasena

class Jugador:
    """Clase para el manejo de usuarios del juego."""

    def __init__(self, nombre=None, contrasena=None):
        """Inicializa la clase Jugador con usuario opcionalmente activo."""
        self.usuario_actual = nombre
        self.contrasena = contrasena

    def crear_cuenta(self, usuario, contraseña):
        """Crea una nueva cuenta de usuario."""
        if usuario == "" and contraseña == "":
            return "Las credenciales no pueden estar vacías"
        if not usuario:
            return "El usuario no puede estar vacío"
        if not contraseña:
            return "La contraseña no puede estar vacía"

        # Intenta crear el usuario en la base de datos
        try:
            crear_usuario(usuario, contraseña)
            return "Cuenta creada exitosamente"
        except Exception as e:
            return str(e)  # Devuelve el error si no se pudo crear
      
    def cambiar_contraseña(self, nueva_contraseña):
        """Cambia la contraseña del usuario actual."""
        if not self.usuario_actual:
            return "No hay sesión activa"
        
        if nueva_contraseña is None:
            raise TypeError("La contraseña no puede ser None")
        
        if not isinstance(nueva_contraseña, str):
            raise TypeError("La contraseña debe ser un string")
        
        if nueva_contraseña == "":
            return "La contraseña no puede estar vacía"
        
        if nueva_contraseña == self.contrasena:
            return "La nueva contraseña no puede ser igual a la actual"

        if len(nueva_contraseña) < 6:
            return "Contraseña demasiado corta"
        
        if len(nueva_contraseña) > 100:
            return "Contraseña demasiado larga"

        actualizado = actualizar_contrasena(self.usuario_actual, nueva_contraseña)
        if actualizado:
            self.contrasena = nueva_contraseña
            return "Contraseña cambiada exitosamente"
        else:
            return "Error al actualizar la contraseña"  

    def iniciar_sesion(self, usuario, contraseña):
        """Inicia sesión con las credenciales dadas."""
        if usuario is None or contraseña is None:
            raise TypeError("Los valores no pueden ser None")
        if not usuario and not contraseña:
            return "Credenciales incompletas"
        if not usuario:
            return "Usuario no puede estar vacío"
        if not contraseña:
            return "Contraseña no puede estar vacía"

        # Obtiene el usuario de la base de datos
        usuario_db = obtener_usuario(usuario)
        if usuario_db is None:
            return "Usuario no encontrado"
        if usuario_db.contrasena != contraseña:
            return "Contraseña incorrecta"

        self.usuario_actual = usuario
        return "Sesión iniciada"

    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual."""
        if self.usuario_actual:
            print(f"👋 {self.usuario_actual}, has cerrado sesión.")
            self.usuario_actual = None
        else:
            print("⚠ No hay ninguna sesión activa.")
