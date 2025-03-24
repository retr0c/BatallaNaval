
class Jugador:
    def __init__(self, usuario=None, contraseña=None):
        self.usuarios = {}
        self.usuario_actual = None
        if usuario and contraseña:
            self.usuarios[usuario] = contraseña

    def crear_cuenta(self, usuario, contraseña):
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
        if self.usuario_actual:
            print(f"👋 {self.usuario_actual}, has cerrado sesión.")
            self.usuario_actual = None
        else:
            print("⚠ No hay ninguna sesión activa.")

    def cambiar_contraseña(self, nueva_contraseña):
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