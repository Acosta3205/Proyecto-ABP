from pymongo import MongoClient

# Conexión a la base de datos
def get_db():
    # Establece el cliente de MongoDB
    client = MongoClient("mongodb://10.102.10.241:27017/")
    # Establece la base de datos a utilizar
    db = client["Restaurante"]
    # Devuelve la base de datos
    print("Conexión a la base de datos establecida.")
    return db