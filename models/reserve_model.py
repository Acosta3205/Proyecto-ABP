# Importar BaseModel desde pydantic
from pydantic import BaseModel

# Importar datetime
from datetime import datetime, date, time

# Conexión a la base de datos
from services.mongo_service import get_db

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
    if "reservas" in db.list_collection_names():
        print("La tabla 'reservas' ya existe.")
    else:
        db.create_collection("reservas")
        # Informar al usuario
        print("La tabla reservas se ha creado correctamente.")    