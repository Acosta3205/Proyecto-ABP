#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar la libreria pymongo
from pymongo import DESCENDING

from views.four_view import id_fila_eliminar

def id_nuevo_cliente(db):
    """Función que devuelve el ID del nuevo cliente creado sumando 1 al ID del cliente anterior.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.

    Returns:
        int: El ID del nuevo cliente.
    """
    # Almacenar la colección "Clientes" en la variable clientes
    clientes = db.clientes
    # Buscar el último cliente ordenado por el campo 'id' de forma descendente
    ultimo_cliente = clientes.find().sort("id", DESCENDING).limit(1)

    # Convertir la consulta a una lista de Python
    ultimo_cliente_lista = list(ultimo_cliente)
    
    # Si hay un cliente, devolver el ID del cliente, si no, devolver 0
    if ultimo_cliente_lista:
        return ultimo_cliente_lista[0]["id"]
    else:
        return 0

def id_nueva_reserva(db):
    """Función que devuelve el ID de la nueva reserva creada sumando 1 al ID de la reserva anterior.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.

    Returns:
        int: El ID de la nueva reserva.
    """
    # Almacenar la colección "Reservas" en la variable reservas
    reservas = db.reservas
    # Buscar la última reserva ordenada por el campo 'id' de forma descendente
    ultima_reserva = reservas.find().sort("id", DESCENDING).limit(1)

    # Convertir la consulta a una lista de Python
    ultima_reserva_lista = list(ultima_reserva)
    
    # Si hay una reserva, devolver el ID de la reserva, si no, devolver 0
    if ultima_reserva_lista:
        return ultima_reserva_lista[0]["id"]
    else:
        return 0

# Función que comprueba las mesas adecuadas para el número de comensales
def mostrar_mesas(db, num_comensales):
    """Función que devuelve una lista con las mesas adecuadas para el número de comensales.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
        num_comensales (str): El número de comensales.

    Returns:
        list: Una lista con las mesas adecuadas para el número de comensales.
    """
    # Si no se proporciona el número de comensales, devolver una lista vacía
    if not num_comensales:
        return []

    # Obtener todas las mesas
    mesas = db.mesas
    # Buscar las mesas donde la capacidad sea mayor o igual que num_comensales
    mesas_adecuadas = mesas.find({"capacidad": {"$gte": int(num_comensales)}})

    # Obtener el número de mesa de cada una de las mesas adecuadas
    lista_mesas_adecuadas = [mesa["numero_mesa"] for mesa in mesas_adecuadas]

    # Devolver la lista de mesas adecuadas
    return lista_mesas_adecuadas

def mostrar_nota_mesa(db, num_mesa):
    """Función que devuelve la nota de una mesa.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
        num_mesa (str): El número de mesa.

    Returns:
        str: La nota de la mesa.
    """
    # Almacenar la colección "Mesas" en la variable mesas
    mesas = db.mesas

    # Buscar la nota de una mesa específica por su numero de mesa
    mesa = mesas.find_one({"numero_mesa": int(num_mesa)}, {"ubicacion": 1})
    
    # Devolver la nota de la mesa
    return mesa["ubicacion"] if mesa else None

def buscar_id_cliente(db, nombre, telefono):
    """Busca el ID del cliente relacionado con el nombre y teléfono proporcionados.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (str): El nombre del cliente.
        telefono (str): El teléfono del cliente.

    Returns:
        int: El ID del cliente.
    """
    # Almacenar la colección "Clientes" en la variable clientes
    clientes = db.clientes

    # Buscar el ID del cliente relacionado con el nombre y teléfono proporcionados
    cliente = clientes.find_one({"nombre": nombre, "telefono": telefono})

    # Devolver el ID del cliente
    return cliente["id"]

def buscar_reservas(db, nombre, telefono):
    """Primero busca el ID del cliente relacionado con el nombre y teléfono proporcionados, luego busca las reservas relacionadas con ese ID en la base de datos.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (str): El nombre del cliente.
        telefono (str): El teléfono del cliente.

    Returns:
        list: Una lista con las reservas relacionadas con el ID del cliente.
    """
    # Almacenar la colección "Clientes" y "Reservas" en las variables clientes y reservas
    clientes = db.clientes
    reservas = db.reservas
    # Busca las reservas relacionadas con el ID del cliente asociado al nombre y teléfono proporcionados
    try:
        # Obtener el ID del cliente
        id_cliente = clientes.find_one({"nombre": nombre, "telefono": telefono})["id"]
        
        # Buscar las reservas relacionadas con el ID del cliente
        reservas_cliente = reservas.find({"id_cliente": id_cliente})

        # Convertir la consulta a una lista de Python
        reservas_cliente_lista = list(reservas_cliente)

        # Devolver la lista de reservas
        return reservas_cliente_lista
    
    # Si no se encuentra el cliente, devolver una lista vacía
    except TypeError:
        return []

def comprobar_cliente_existente(db, nombre, telefono, email, direccion):
    """Comprueba si un cliente ya existe en la base de datos. En caso de que no exista, devuelve False. En caso contrario, devuelve True.

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (str): El nombre del cliente.
        telefono (str): El teléfono del cliente.
        email (str): El correo electrónica del cliente.
        direccion (str): La direcció del cliente.

    Returns:
        bool: True si el cliente ya existe en la base de datos, False en caso contrario.
    """
    # Almacenar la colección "Clientes" en la variable clientes
    clientes = db.clientes

    # Buscar el cliente en la base de datos
    cliente = clientes.find_one({"nombre": nombre, "telefono": telefono, "email": email, "direccion": direccion})

    # Devolver True si el cliente existe, False en caso contrario
    return True if cliente else False

def EliminarReservaSelecionada(db, id_fila_eliminar):
    """Elimina una reserva de la base de datos mediante su ID. 

    Args:
        db (pymongo.database.Database): La base de datos de MongoDB.
        id_fila_eliminar (int): El ID de la reserva a eliminar.
    """

    # Almacena la colección "Reservas" en la variable reservas
    reservas = db.reservas

    # Realiza la eliminación basada en el ID de la reserva
    reservas.delete_one({"id": id_fila_eliminar})

def CargarDatosReserva(page, db, id_reserva):
    """Carga los datos de una reserva de la base de datos mediante su ID. 

    Args:
        page (ft.Page): La página actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        id_reserva (int): El ID de la reserva a cargar.
    
    Returns:
        dict: Un diccionario con los datos de la reserva.
    """
    # Almacena la colección "Reservas" en la variable reservas
    reservas = db.reservas

    # Busca la reserva por su ID y obtiene los datos
    reserva = reservas.find_one({"id": id_reserva})

    # Devuelve la reserva en un diccionario
    return reserva
