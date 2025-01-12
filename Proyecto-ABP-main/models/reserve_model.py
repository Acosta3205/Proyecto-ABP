# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time


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
    # Crear las colecciones
    # Comprobar si las colecciones existen
    if "reservas" in db.list_collection_names():
        print("La tabla 'reservas' ya existe.")
    else:
        db.create_collection("reservas")

        # Informar al usuario
        print("La tabla reservas se ha creado correctamente.")   