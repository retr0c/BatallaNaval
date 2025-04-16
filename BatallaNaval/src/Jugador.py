class Jugador:
    """Clase para el manejo de usuarios del juego."""

    def __init__(self, usuario=None, contraseña=None):
        """
        Inicializa la clase Jugador con un usuario opcional.

        Args:
            usuario (str, optional): Nombre del usuario.
            contraseña (str, optional): Contraseña del usuario.
        """
        self.usuarios = {}
        self.usuario_actual = None
        if usuario and contraseña:
            self.usuarios[usuario] = contraseña

    def crear_cuenta(self, usuario, contraseña):
        """
        Crea una nueva cuenta de usuario.

        Args:
            usuario (str): Nombre del usuario.
            contraseña (str): Contraseña del usuario.

        Returns:
            str: Mensaje indicando el resultado de la operación.
        """
        if usuario == "" and contraseña == "":
            return "Las credenciales no pueden estar vacías"
        if not usuario:
            return "El usuario no puede estar vacío"
        if not contraseña:
            return "La contraseña no puede estar vacía"
        if usuario in self.usuarios:
            return "El usuario ya existe"

        self.usuarios[usuario] = contraseña
        return "Cuenta creada exitosamente"

    def iniciar_sesion(self, usuario, contraseña):
        """
        Inicia sesión con las credenciales dadas.

        Args:
            usuario (str): Nombre del usuario.
            contraseña (str): Contraseña del usuario.

        Returns:
            str: Mensaje indicando el resultado del intento de inicio de sesión.

        Raises:
            TypeError: Si usuario o contraseña son None.
        """
        if usuario is None or contraseña is None:
            raise TypeError("Los valores no pueden ser None")
        if not usuario and not contraseña:
            return "Credenciales incompletas"
        if not usuario:
            return "Usuario no puede estar vacío"
        if not contraseña:
            return "Contraseña no puede estar vacía"
        if usuario not in self.usuarios:
            return "Usuario no encontrado"
        if self.usuarios[usuario] != contraseña:
            return "Contraseña incorrecta"

        self.usuario_actual = usuario
        return "Sesión iniciada"

    def cerrar_sesion(self):
        """
        Cierra la sesión del usuario actual.
        """
        if self.usuario_actual:
            print(f"👋 {self.usuario_actual}, has cerrado sesión.")
            self.usuario_actual = None
        else:
            print("⚠ No hay ninguna sesión activa.")

    def cambiar_contraseña(self, nueva_contraseña):
        """
        Cambia la contraseña del usuario actual.

        Args:
            nueva_contraseña (str): La nueva contraseña.

        Returns:
            str: Mensaje indicando el resultado de la operación.

        Raises:
            TypeError: Si la contraseña es None o no es una cadena.
        """
        if nueva_contraseña is None:
            raise TypeError("La contraseña no puede ser None")
        if not nueva_contraseña:
            return "La contraseña no puede estar vacía"
        if not isinstance(nueva_contraseña, str):
            raise TypeError("La contraseña debe ser una cadena de texto")
        if len(nueva_contraseña) < 6:
            return "Contraseña demasiado corta"
        if len(nueva_contraseña) > 100:
            return "Contraseña demasiado larga"

        for usuario, contraseña_actual in self.usuarios.items():
            if nueva_contraseña == contraseña_actual:
                return "La nueva contraseña no puede ser igual a la actual"
            self.usuarios[usuario] = nueva_contraseña
            return "Contraseña cambiada exitosamente"

        return "No hay usuarios registrados"
