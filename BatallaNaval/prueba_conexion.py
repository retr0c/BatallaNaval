
try:
    from base_datos.db import crear_usuario
    print("Importación exitosa")
except ModuleNotFoundError as e:
    print(f"Error de importación: {e}")
