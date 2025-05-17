from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Usuario(Base):
       __tablename__ = "usuarios"
       
       id = Column(Integer, primary_key=True)
       nombre = Column(String(100), nullable=False, unique=True)
       contrasena = Column(String(100), nullable=False)
       
       def __repr__(self):
           return f"<Usuario(nombre='{self.nombre}')>"

class Puntuacion(Base):
       __tablename__ = "puntuaciones"
       
       id = Column(Integer, primary_key=True)
       usuario_id = Column(Integer, ForeignKey('usuarios.id'))
       puntaje = Column(Integer, nullable=False)
       
       def __repr__(self):
         return f"<Puntuacion(usuario_id={self.usuario_id}, puntaje={self.puntaje})>"