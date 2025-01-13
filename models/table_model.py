#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Definir la tabla "mesas"
class Mesas(BaseModel):
    id: int
    numero: int
    capacidad: int
    ubicacion: str

def crear_tabla_mesas(db):
    """Crea la tabla "mesas" en la base de datos si no existe.
    
    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    # Si la tabla 'mesas' ya existe, no se crea y se informa al usuario
    if "mesas" in db.list_collection_names():
        # Informar al usuario
        print("La tabla 'mesas' ya existe.")
    # Si la tabla 'mesas' no existe, se crea y se informa al usuario
    else:
        # Crear la colección
        db.create_collection("mesas")

        # Informar al usuario
        print("La tabla mesas se ha creado correctamente.")
    