#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar la libreria pymongo
from pymongo import MongoClient

# Importar la dirección de la base de datos
from utils.config import mongo_uri

# Conexión a la base de datos
def get_db():
    """Función que establece la conexión a la base de datos.

    Returns:
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    # Establece el cliente de MongoDB mediante el URI almacenado en el archivo config.py en la variable mongo_uri
    client = MongoClient(mongo_uri)
    # Establece la base de datos a utilizar
    db = client["Restaurante"]
    # Mensaje por la consola de la conexión a la base de datos
    print("Conexión a la base de datos establecida.")
    # Devuelve la base de datos
    return db