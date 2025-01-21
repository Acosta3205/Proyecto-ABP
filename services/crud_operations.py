from services.querys import id_nuevo_cliente, id_nueva_reserva, comprobar_cliente_existente, buscar_id_cliente

# Lista que almacena el ID del cliente actual una vez se pasa a la configuración de la reserva
cliente_actual = []

# Insertar las mesas a partir de un .json
def insertar_mesas_json(db):
  """Importa las mesas a partir de un listado de diccionarios en formato JSON. Comprueba si las mesas ya existen en la base de datos y las inserta solo en el caso de que no existan.
  
  Args:
      db (pymongo.database.Database): La base de datos MongoDB.
  """
  # Listado de mesas a insertar
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

  # Intentar insertar las mesas en la colección "Mesas" de la base de datos
  try:
    # Listas para almacenar las mesas insertadas y las ya existentes
    mesas_insertadas = []
    mesas_existentes = []

    # Comprobar si cada una de las mesas ya existe en la base de datos
    for mesa in mesas:
      # Si la mesa no existe, insertarla
      if db.mesas.find_one({"id": mesa["id"]}) is None:
        db.mesas.insert_one(mesa)
        mesas_insertadas.append(mesa["id"])
      # Si la mesa ya existe, guardar su ID en la lista para mostrarlo por la consola a modo informativo
      else:
        mesas_existentes.append(mesa["id"])

    # Mostrar por la consola las mesas insertadas
    if len(mesas_insertadas) > 0:
      print(f"Se han insertado las mesas: {mesas_insertadas}")
    
    # Mostrar por la consola las mesas ya existentes
    if len(mesas_existentes) > 0:
      print(f"Las mesas ya existentes en la base de datos eran: {mesas_existentes}")
  
  # En caso de error, mostrar por la consola el error producido
  except Exception as e:
    print(f"Error al insertar las mesas en la base de datos: {e}")

def insertar_datos_clientes(page, db, nombre, telefono, email, direccion):
  """Recibe los datos del formulario de datos de contacto del cliente y los inserta en la base de datos, en caso de que el cliente no exista.
  
  Args:
    page (str): La página actual de la aplicación.
    db (pymongo.database.Database): La base de datos de MongoDB.
    nombre (str): El nombre del cliente.
    telefono (str): El teléfono del cliente.
    email (str): El correo electrónico del cliente.
    direccion (str): La dirección del cliente.
  """
  # Intentar insertar los datos en la colección "Clientes"
  try:
    # Si el cliente no existe en la base de datos se insertan los datos
    if not comprobar_cliente_existente(db, nombre, telefono, email, direccion):
      # Vaciar la lista de ID
      cliente_actual.clear()
      # Generar un nuevo ID para el cliente
      id_cliente = id_nuevo_cliente(db) + 1
      cliente_actual.append(id_cliente)
      # Insertar los datos en la colección "Clientes"
      db.clientes.insert_one({"id": id_cliente, "nombre": nombre, "telefono": telefono, "email": email, "direccion": direccion})
      # Mensaje por la consola de la inserción de los datos
      print("Los datos se han insertado correctamente en la base de datos.")

    # Si el cliente ya existe en la base de datos no se insertan los datos y se muestra un mensaje por la consola a modo informativo
    else:
      # Vaciar la lista de ID
      cliente_actual.clear()
      # Recuperar el ID del cliente existente
      cliente_actual.append(buscar_id_cliente(db, nombre, telefono))
      # Mensaje por la consola de la no inserción de los datos
      print("El cliente ya existe en la base de datos y por lo tanto no se ha insertado.")

  # En caso de error, mostrar por la consola el error producido
  except Exception as e:
    print(f"Error al insertar los datos en la base de datos: {e}")


def insertar_datos_reserva(db, NumMesa, NumPerson, Hora, Fecha, Notas):
  """Recibe los datos del formulario de la creación de una reserva y los inserta en la base de datos.
  
  Args:
    db (pymongo.database.Database): La base de datos de MongoDB.
    NumMesa (str): El número de mesa.
    NumPerson (str): El número de personas.
    Hora (str): La hora de la reserva.
    Fecha (str): La fecha de la reserva.
    Notas (str): Las notas de la reserva.
  """
  id_reserva = id_nueva_reserva(db) + 1
  try:
    # Insertar los datos en la colección "Reservas"
    db.reservas.insert_one({"id": id_reserva, "id_cliente": cliente_actual[0], "id_mesa": int(NumMesa), "fecha": Fecha, "hora": Hora, "num_personas": NumPerson, "estado": "Confirmada", "notas": Notas})
    print("Los datos se han insertado correctamente en la base de datos.")

  # En caso de error, mostrar por la consola el error producido
  except Exception as e:
    print(f"Error al insertar los datos en la base de datos: {e}")

def GuardarReserva(db, NumMesa, Fecha, Hora, NumPerson, Notas, id_reserva):
  """Actualiza los datos de una reserva ya existente en la base de datos con los nuevos datos recibidos.
  
  Args:
    db (pymongo.database.Database): La base de datos de MongoDB.
    NumMesa (str): El número de mesa.
    Fecha (str): La fecha de la reserva.
    Hora (str): La hora de la reserva.
    NumPerson (str): El número de personas.
    Notas (str): Las notas de la reserva.
    id_reserva (int): El ID de la reserva.
  """
  try:
    # Actualizar los datos en la colección "Reservas"
    db.reservas.update_one({"id": id_reserva}, {"$set": {"id_mesa": int(NumMesa), "fecha": Fecha, "hora": Hora, "num_personas": NumPerson, "estado": "Confirmada", "notas": Notas}})
    print("Los datos se han actualizado correctamente en la base de datos.")

  # En caso de error, mostrar por la consola el error producido
  except Exception as e:
    print(f"Error al actualizar los datos en la base de datos: {e}")