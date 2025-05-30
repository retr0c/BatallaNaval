class FakeUserRepository:
    def __init__(self):
        self.usuarios = []
    
    def crear_usuario(self, usuario):
        usuario.id = len(self.usuarios) + 1
        self.usuarios.append(usuario)
        return usuario.id

    def obtener_usuario(self, nombre):
        for u in self.usuarios:
            if u.nombre == nombre:
                return u
        return None

    def actualizar_contrasena(self, nombre, nueva_contrasena):
        usuario = self.obtener_usuario(nombre)
        if usuario:
            usuario.contrasena = nueva_contrasena
            return True
        return False

class FakePuntuacionRepository:
    def __init__(self):
        self.puntuaciones = []

    def guardar_puntuacion(self, puntuacion):
        self.puntuaciones.append(puntuacion)
