from services.querys import id_nuevo_cliente, id_nueva_reserva

cliente_actual = []

# Insertar las mesas a partir de un archivo .json
def insertar_mesas_json(db):
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

  """Recibe una lista de mesas y las inserta en la base de datos"""
  try:
    mesas_insertadas = []
    mesas_existentes = []

    # Insertar las mesas desde la lista en la colección "Mesas"
    # Comprobar si cada una de las mesas ya existe en la base de datos
    for mesa in mesas:
      if db.mesas.find_one({"id": mesa["id"]}) is None:
        db.mesas.insert_one(mesa)
        mesas_insertadas.append(mesa["id"])
      else:
        mesas_existentes.append(mesa["id"])

    if len(mesas_insertadas) > 0:
      print(f"Se han insertado las mesas: {mesas_insertadas}")
    
    if len(mesas_existentes) > 0:
      print(f"Las mesas ya existentes en la base de datos eran: {mesas_existentes}")

  except Exception as e:
    print(f"Error al insertar las mesas en la base de datos: {e}")

def insertar_datos_clientes(page, db, nombre, telefono, email, direccion):
  """Recibe los datos del formulario y los inserta en la base de datos"""
  id_cliente = id_nuevo_cliente(db) + 1
  cliente_actual.append(id_cliente)
  try:
    # Insertar los datos en la colección "Clientes"
    db.clientes.insert_one({"id": id_cliente, "nombre": nombre, "telefono": telefono, "email": email, "direccion": direccion})
    print("Los datos se han insertado correctamente en la base de datos.")

  except Exception as e:
    print(f"Error al insertar los datos en la base de datos: {e}")


def insertar_datos_reserva(db, NumMesa, NumPerson, Hora, Fecha, Notas):
  """Recibe los datos del formulario y los inserta en la base de datos"""
  id_reserva = id_nueva_reserva(db) + 1
  try:
    # Insertar los datos en la colección "Reservas"
    db.reservas.insert_one({"id": id_reserva, "id_cliente": cliente_actual[0], "id_mesa": NumMesa, "fecha": Fecha, "hora": Hora, "num_personas": NumPerson, "estado": "Confirmada", "notas": Notas})
    print("Los datos se han insertado correctamente en la base de datos.")

  except Exception as e:
    print(f"Error al insertar los datos en la base de datos: {e}")