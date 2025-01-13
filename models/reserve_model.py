#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Definir la tabla "reservas"
class Reservas(BaseModel):
    id: int
    id_cliente: int
    id_mesa: int
    fecha: date
    hora: time
    num_personas: int
    estado: str
    notas: str

def crear_tabla_reservas(db):
    """Crea la tabla "reservas" en la base de datos MongoDB si no existe.
    
    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    # Si la tabla "reservas" ya existe, no crearla e informar al usuario
    if "reservas" in db.list_collection_names():
        print("La tabla 'reservas' ya existe.")
    # Si la tabla "reservas" no existe, crearla e informar al usuario
    else:
        # Crear la colección
        db.create_collection("reservas")

        # Informar al usuario
        print("La tabla reservas se ha creado correctamente.")   