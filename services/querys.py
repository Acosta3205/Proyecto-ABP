
from pymongo import DESCENDING

from views.four_view import id_fila_eliminar

def id_nuevo_cliente(db):
    clientes = db.clientes
    # Buscar el último cliente ordenado por el campo 'id' de forma descendente
    ultimo_cliente = clientes.find().sort("id", DESCENDING).limit(1)

    # Convertir la consulta a una lista de Python
    ultimo_cliente_lista = list(ultimo_cliente)
    if ultimo_cliente_lista:
        return ultimo_cliente_lista[0]["id"]
    else:
        return 0

def id_nueva_reserva(db):
    reservas = db.reservas
    # Buscar la última reserva ordenada por el campo 'id' de forma descendente
    ultima_reserva = reservas.find().sort("id", DESCENDING).limit(1)

    # Convertir la consulta a una lista de Python
    ultima_reserva_lista = list(ultima_reserva)
    if ultima_reserva_lista:
        return ultima_reserva_lista[0]["id"]
    else:
        return 0

# Función que comprueba las mesas adecuadas para el número de comensales
def mostrar_mesas(db, num_comensales):
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
    mesas = db.mesas
    # Buscar la nota de una mesa específica por su numero de mesa
    mesa = mesas.find_one({"numero_mesa": int(num_mesa)}, {"ubicacion": 1})
    return mesa["ubicacion"] if mesa else None

def buscar_id_cliente(db, nombre, telefono):
    clientes = db.clientes
    cliente = clientes.find_one({"nombre": nombre, "telefono": telefono})

    return cliente["id"]

def buscar_reservas(db, nombre, telefono):
    """Primero busca el ID del cliente relacionado con el nombre y teléfono proporcionados, luego busca las reservas relacionadas con ese ID en la base de datos."""
    # Buscar el ID del cliente
    clientes = db.clientes
    reservas = db.reservas
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
    """Comprueba si un cliente ya existe en la base de datos."""
    clientes = db.clientes
    cliente = clientes.find_one({"nombre": nombre, "telefono": telefono, "email": email, "direccion": direccion})

    return True if cliente else False

def EliminarReservaSelecionada(db, id_fila_eliminar):

    # Accede a la colección de reservas
    reservas = db.reservas

    # Realiza la eliminación basada en el `row_id`
    reservas.delete_one({"id": id_fila_eliminar})

def CargarDatosReserva(page, db, id_reserva):
    # Accede a la colección de reservas
    reservas = db.reservas

    # Busca la reserva por su ID y obtiene los datos
    reserva = reservas.find_one({"id": id_reserva})

    # Devuelve la reserva en un diccionario
    return reserva
