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
    # Crear las colecciones
    # Comprobar si las colecciones existen
    if "clientes" in db.list_collection_names():
        print("La tabla 'clientes' ya existe.")
    else:
        db.create_collection("clientes")

        # Informar al usuario
        print("La tabla clientes se ha creado correctamente.")
