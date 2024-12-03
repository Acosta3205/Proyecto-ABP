# Archivo para establecer conexión con la base de datos "Restaurante" que hemos creado en MongoDB
from pymongo import MongoClient
from utils.config import MONGO_URI

# Conexión a la base de datos
def get_db():
    # Establece el cliente de MongoDB
    client = MongoClient(MONGO_URI)
    # Establece la base de datos a utilizar
    db = client["Restaurante"]
    # Devuelve la base de datos
    return db