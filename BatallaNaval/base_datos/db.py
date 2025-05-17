from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BatallaNaval.base_datos.modelo import Base, Usuario, Puntuacion
from BatallaNaval.base_datos.config import DATABASE_URL

# Configura la conexión a la base de datos
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
 
Session = sessionmaker(bind=engine)

def crear_usuario(nombre, contrasena):
    session = Session()
    nuevo_usuario = Usuario(nombre=nombre, contrasena=contrasena)
    session.add(nuevo_usuario)
    session.commit()
    usuario_id = nuevo_usuario.id
    session.close()
    return usuario_id

def obtener_usuario(nombre):
    session = Session()
    usuario = session.query(Usuario).filter_by(nombre=nombre).first()
    session.close()
    return usuario

def guardar_puntuacion(usuario_id, puntaje):
    session = Session()
    nueva_puntuacion = Puntuacion(usuario_id=usuario_id, puntaje=puntaje)
    session.add(nueva_puntuacion)
    session.commit()
    session.close()
    
def actualizar_contrasena(nombre, nueva_contrasena):
    session = Session()
    usuario = session.query(Usuario).filter_by(nombre=nombre).first()
    if usuario:
        usuario.contrasena = nueva_contrasena
        session.commit()
        session.close()
        return True
    session.close()
    return False    