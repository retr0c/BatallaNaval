# setup_db.py

import psycopg2
from sqlalchemy import create_engine
from BatallaNaval.base_datos.modelo import Base
from BatallaNaval.base_datos.config import DATABASE_URL

# Configuraciones (puedes cambiar esto si tu PostgreSQL no usa estos datos por defecto)
DB_NAME = "batalla_naval"
DB_USER = "naval_use"
DB_PASSWORD = "tu_clave_segura"
DB_HOST = "localhost"
DB_PORT = "5432"
POSTGRES_SUPERUSER = "postgres"
POSTGRES_PASSWORD = "felipe12ortiz22"  # Cambia esto si tu clave de postgres es distinta

def crear_base_datos():
    print("🔧 Conectando como superusuario para crear base de datos y usuario...")

    conexion = psycopg2.connect(
        dbname="postgres",
        user=POSTGRES_SUPERUSER,
        password=POSTGRES_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conexion.autocommit = True
    cursor = conexion.cursor()

    # Crear usuario si no existe
    cursor.execute(f"DO $$ BEGIN IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '{DB_USER}') THEN CREATE ROLE {DB_USER} WITH LOGIN PASSWORD '{DB_PASSWORD}'; END IF; END $$;")

    # Crear base de datos si no existe
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    existe = cursor.fetchone()
    if not existe:
        cursor.execute(f"CREATE DATABASE {DB_NAME} OWNER {DB_USER};")
        print(f"✅ Base de datos '{DB_NAME}' creada.")
    else:
        print(f"ℹ️ La base de datos '{DB_NAME}' ya existe.")

    conexion.close()

def crear_tablas():
    print("🗂️ Creando tablas con SQLAlchemy...")
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("✅ Tablas creadas exitosamente.")

if __name__ == "__main__":
    crear_base_datos()
    crear_tablas()
    print("🚀 Configuración completa.")
