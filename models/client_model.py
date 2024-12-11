# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Conexión a la base de datos
from services import get_db

# Definir la tabla "clientes"
class Clientes(BaseModel):
    id: int
    nombre: str
    telefono: int
    email: str
    direccion: str

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

        # Informar al usuario
        print("La tabla clientes se ha creado correctamente.")