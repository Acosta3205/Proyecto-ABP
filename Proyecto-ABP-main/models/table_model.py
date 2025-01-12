# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Conexión a la base de datos

class Mesas(BaseModel):
    id: int
    numero: int
    capacidad: int
    ubicacion: str

def crear_tabla_mesas(db):
    # Crear las colecciones
    # Comprobar si las colecciones existen

    if "mesas" in db.list_collection_names():
        print("La tabla 'mesas' ya existe.")
    else:
        db.create_collection("mesas")

        # Informar al usuario
        print("La tabla mesas se ha creado correctamente.")
    