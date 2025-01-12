from pymongo import MongoClient

# Importar la dirección de la base de datos
from utils.config import mongo_uri

# Conexión a la base de datos
def get_db():
    # Establece el cliente de MongoDB
    client = MongoClient(mongo_uri)
    # Establece la base de datos a utilizar
    db = client["Restaurante"]
    # Devuelve la base de datos
    print("Conexión a la base de datos establecida.")
    return db