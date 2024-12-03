# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Importar el archivo de conexión a la base de datos
from services.mongo_service import get_db

class Clientes(BaseModel):
    id: int
    nombre: str
    telefono: int
    email: str
    direccion: str

class Mesas(BaseModel):
    id: int
    numero: int
    capacidad: int
    ubicacion: str

class Reservas(BaseModel):
    id: int
    id_cliente: int
    id_mesa: int
    fecha: date
    hora: time
    estado: str
    notas: str

# Realizar la creación de las colecciones a partir de los modelos
if __name__ == "__main__":
    # Obtener la base de datos
    db = get_db()

    # Crear las colecciones
    # Comprobar si las colecciones existen
    if "clientes" in db.list_collection_names():
        print("La tabla 'clientes' ya existe.")
    else:
        db.create_collection("clientes")

    if "mesas" in db.list_collection_names():
        print("La tabla 'mesas' ya existe.")
    else:
        db.create_collection("mesas")

    if "reservas" in db.list_collection_names():
        print("La tabla 'reservas' ya existe.")
    else:
        db.create_collection("reservas")

    # Informar al usuario
    print("Las tablas se han creado correctamente.")

    