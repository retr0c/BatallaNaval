from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BatallaNaval.base_datos.modelo import Base, Usuario, Puntuacion
from BatallaNaval.base_datos.config import DATABASE_URL

# Configura la conexión a la base de datos
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
 
Session = sessionmaker(bind=engine)

def crear_usuario(nombre, contrasena):
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        nombre (str): Nombre de usuario.
        contrasena (str): Contraseña del usuario.

    Returns:
        int: ID del usuario creado.
    """
    session = Session()
    nuevo_usuario = Usuario(nombre=nombre, contrasena=contrasena)
    session.add(nuevo_usuario)
    session.commit()
    usuario_id = nuevo_usuario.id
    session.close()
    return usuario_id

def obtener_usuario(nombre):
    """
    Obtiene un objeto Usuario dado su nombre.

    Args:
        nombre (str): Nombre del usuario.

    Returns:
        Usuario or None: Objeto Usuario si se encuentra, None si no existe.
    """
    session = Session()
    usuario = session.query(Usuario).filter_by(nombre=nombre).first()
    session.close()
    return usuario

def guardar_puntuacion(usuario_id, puntaje):
    """
    Guarda una nueva puntuación para un usuario.

    Args:
        usuario_id (int): ID del usuario.
        puntaje (int): Puntaje obtenido.
    """
    session = Session()
    nueva_puntuacion = Puntuacion(usuario_id=usuario_id, puntaje=puntaje)
    session.add(nueva_puntuacion)
    session.commit()
    session.close()
    
def actualizar_contrasena(nombre, nueva_contrasena):
    """
    Actualiza la contraseña de un usuario.

    Args:
        nombre (str): Nombre del usuario.
        nueva_contrasena (str): Nueva contraseña a establecer.

    Returns:
        bool: True si se actualizó correctamente, False si el usuario no existe.
    """
    session = Session()
    usuario = session.query(Usuario).filter_by(nombre=nombre).first()
    if usuario:
        usuario.contrasena = nueva_contrasena
        session.commit()
        session.close()
        return True
    session.close()
    return False

def obtener_puntuaciones(): 
    pass
