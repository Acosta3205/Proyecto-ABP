#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Definir la tabla "clientes"
class Clientes(BaseModel):
    id: int
    nombre: str
    telefono: int
    email: str
    direccion: str

    class Config:
        from_attributes = True

def crear_tabla_clientes(db):
    """Crea la tabla "clientes" en la base de datos de MongoDB si no existe.
    
    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    # Si la tabla "clientes" ya existe en la base de datos no se crea y se informa al usuario
    if "clientes" in db.list_collection_names():
        print("La tabla 'clientes' ya existe.")
    # Si la tabla "clientes" no existe en la base de datos se crea y se informa al usuario
    else:
        # Crear la colección
        db.create_collection("clientes")

        # Informar al usuario
        print("La tabla clientes se ha creado correctamente.")
