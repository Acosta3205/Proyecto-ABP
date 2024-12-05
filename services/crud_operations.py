# Importar las librerias necesarias
from mongo_service import get_db

mesas = [{
    "id": 1,
    "numero_mesa": 1,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 2,
    "numero_mesa": 2,
    "capacidad": 2,
    "ubicacion": "Interior"
  },
  {
    "id": 3,
    "numero_mesa": 3,
    "capacidad": 6,
    "ubicacion": "Jardín"
  },
  {
    "id": 4,
    "numero_mesa": 4,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 5,
    "numero_mesa": 5,
    "capacidad": 2,
    "ubicacion": "Interior"
  },
  {
    "id": 6,
    "numero_mesa": 6,
    "capacidad": 6,
    "ubicacion": "Jardín"
  },
  {
    "id": 7,
    "numero_mesa": 7,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 8,
    "numero_mesa": 8,
    "capacidad": 2,
    "ubicacion": "Interior"
  },
  {
    "id": 9,
    "numero_mesa": 9,
    "capacidad": 6,
    "ubicacion": "Jardín"
  },
  {
    "id": 10,
    "numero_mesa": 10,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 11,
    "numero_mesa": 11,
    "capacidad": 2,
    "ubicacion": "Interior"
  },
  {
    "id": 12,
    "numero_mesa": 12,
    "capacidad": 6,
    "ubicacion": "Jardín"
  },
  {
    "id": 13,
    "numero_mesa": 13,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 14,
    "numero_mesa": 14,
    "capacidad": 2,
    "ubicacion": "Interior"
  },
  {
    "id": 15,
    "numero_mesa": 15,
    "capacidad": 6,
    "ubicacion": "Jardín"
  },
  {
    "id": 16,
    "numero_mesa": 16,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 17,
    "numero_mesa": 17,
    "capacidad": 2,
    "ubicacion": "Interior"
  },
  {
    "id": 18,
    "numero_mesa": 18,
    "capacidad": 6,
    "ubicacion": "Jardín"
  },
  {
    "id": 19,
    "numero_mesa": 19,
    "capacidad": 4,
    "ubicacion": "Terraza"
  },
  {
    "id": 20,
    "numero_mesa": 20,
    "capacidad": 2,
    "ubicacion": "Interior"
  }]

# Insertar las mesas a partir de un archivo .json
def insertar_mesas_json(mesas):
  """Recibe una lista de mesas y las inserta en la base de datos"""
  try:
    # Obtener la base de datos
    db  = get_db()

    # Insertar las mesas desde la lista en la colección "Mesas"
    db.mesas.insert_many(mesas)
    print("Las mesas se han insertado correctamente en la base de datos.")

  except Exception as e:
    print(f"Error al insertar las mesas en la base de datos: {e}")

# Insertar las mesas
insertar_mesas_json(mesas)