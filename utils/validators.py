#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------
import flet as ft

#-------------------------------------------------------
# Importación de las vistas necesarias
#-------------------------------------------------------
from views.fifth_view import SelecionarMesaHora
from views.main_view import main
from views.third_view import TablaReservas, generar_tabla_reservas_modificar
from views.four_view import TablaReservas2, generar_tabla_reservas_eliminar
from views.sixth_view import ModificarReserva

#-------------------------------------------------------
# Importación de las consultas necesarias
#-------------------------------------------------------
from services.crud_operations import insertar_datos_clientes, insertar_datos_reserva , GuardarReserva
from services.querys import buscar_reservas, EliminarReservaSelecionada

#-----------------------------------------------------------------
# Validaciones de todos los campos nesesarios para el programa 
#-----------------------------------------------------------------

# Validar el nombre
# --------------------
def validar_nombre(nombre: str):
    """Comprueba que el nombre proporcionado tiene entre 1 y 20 caracteres y que no sean dígitos.
    
    Args:
        nombre (str): El nombre del cliente.

    Returns:
        str: None si el nombre es correcto, un mensaje de error si no lo es.
    """
    while True:
        # Comprobar que el nombre no este vacio
        if len(nombre) == 0:
            return 'El nombre no puede estar vacio'
        # Comprobar que el nombre tenga entre 1 y 20 caracteres
        if not (0 < len(nombre) <= 20):
            return 'El nombre debe tener entre 1 y 20 caracteres'
        # Comprobar que el nombre no contenga dígitos
        elif not nombre.replace(' ', '').isalpha():
            return 'El nombre no puede contener dígitos'
        # Si el nombre es correcto, sale del bucle
        else:
            return None                        

# Validar el telefono
# -----------------------
def validar_telefono(telefono: int):
    """Comprueba que el teléfono proporcionado tiene 9 digitos.
    
    Args:
        telefono (int): El telefono del cliente.

    Returns:
        str: None si el telefono es correcto, un mensaje de error si no lo es.
    """
    while True:
        # Comprobar que el telefono no este vacio
        if len(telefono) == 0:
            return 'El telefono no puede estar vacio'
        # Comprobar que el telefono tenga 9 caracteres
        if not len(telefono) == 9:
            return 'El telefono tiene que tener 9 caracteres'
        # Comprobar que el telefono tiene que ser un numero
        elif not telefono.isdigit():
            return 'El telefono tiene que ser un numero'
        # Si el teléfono es correcto, sale del bucle
        else:
            return None

# Validar el email
# --------------------
def validar_email(email: str):
    """Comprueba que el email proporcionado tiene el formato correo@dominio.com.
    
    Args:
        email (str): El email del cliente.

    Returns:
        str: None si el email es correcto, un mensaje de error si no lo es.
    """
    # Comprobar que el email no este vacío
    if len(email) == 0:
        return "El email no puede estar vacío. Por favor, introduzca de nuevo el email."
    # Comprobar que el email tenga un @ y un .
    elif email.count("@") != 1 or email.count(".") != 1:
        return "El email debe tener un @ y un ."
    # Comprobar que el email tenga el formato correo@dominio.
    elif len(email.split("@")[0]) == 0 or len(email.split("@")[1]) == 0:
        return "El email debe tener el formato correo@dominio."
    # Comprobar que el email tenga el formato correo@dominio.com
    elif len(email.split("@")[1].split(".")[0]) == 0 or len(email.split("@")[1].split(".")[1]) == 0:
        return "El email debe tener el formato correo@dominio.com"
    # Si el email es correcto, sale del bucle
    else:
        return None

# Validar la direccion
# ------------------------
def validar_direccion(direccion: str):
    """Comprueba que la direccion proporcionada no este vacio.
    
    Args:
        direccion (str): La direccion del cliente.

    Returns:
        str: None si la direccion es correcta, un mensaje de error si no lo es.
    """
    # Comprobar que la direccion no este vacia
    if len(direccion) == 0:
        return "La direccion no puede estar vacia."
    # Si la direccion es correcta, sale del bucle
    else:
        return None

# Validar el numero de mesa 
# -----------------------------
def Validar_num_mesa(NumMesa: int):
    """Comprobar que el campo solo contenga numeros.
    
    Args:
        NumMesa (int): El numero de mesa.

    Returns:
        str: None si el numero de mesa es correcto, un mensaje de error si no lo es.
    """
    if not NumMesa:
        return "Debe seleccionar una mesa para la reserva."
    else:
        return None

# Validar el numero de personas
# ---------------------------------
def Validar_num_personas(NumPerson):
    """Comprobar que el campo solo contenga numeros.
    
    Args:
        NumPerson (int): El numero de personas.

    Returns:
        str: None si el numero de personas es correcto, un mensaje de error si no lo es.
    """
    if NumPerson == "":
        return "Introduzca el numero de personas para la reserva"
    elif not NumPerson.isdigit():
        return "El campo de personas solo puede contener numeros."
    else:
        return None

# Validar la hora
# -------------------
def ValidarHora(Hora: str):
    """"Comprobar que la hora esté en el rango de 8:00 a 20:00.
    
    Args:
        Hora (str): La hora de la reserva.

    Returns:
        str: None si la hora es correcta, un mensaje de error si no lo es.
    """
    if Hora == "":
        return "Introduzca una hora para la reserva"
    elif int(Hora.split(":")[0]) < 8 or int(Hora.split(":")[0]) > 20:
        return "El horario de reservas es de 8:00 a 20:00"
    else:
        return None

# Validar la fecha
# ----------------------
def ValidarFecha(Fecha: str):
    """"Comprobar que la fecha no este vacia.
    
    Args:
        Fecha (str): La fecha de la reserva.

    Returns:
        str: None si la fecha es correcta, un mensaje de error si no lo es.
    """
    if Fecha == "":
        return "Introduzca una fecha para la reserva"
    else:
        return None

# Validar las notas
# ----------------------
def ValidarNotas(Notas: str):
    """"Comprobar que la nota no este vacia.
    
    Args:
        Notas (str): Las notas de la reserva.

    Returns:
        str: None si la nota es correcta, un mensaje de error si no lo es.
    """
    if Notas == "":
        return "El campo de notas no puede estar vacio. Debes selecionar una mesa"
    else:
        return None

#-----------------------------------------------------------------
# Funciones para el manejo de los cuadros de diálogo
#-----------------------------------------------------------------

# Función para cerrar el cuadro de diálogo
# --------------------------------------------
def close_dialog(page):
    """Función para cerrar el cuadro de diálogo.
    
    Args:
        page (ft.Page): La pagina actual.
    """
    # Si el cuadro de diálogo existe, lo cerramos
    if page.dialog != None:
        page.dialog.open = False
        # Actualizamos la pantalla
        page.update()

# Función para cerrar el cuadro de diálogo y volver a la pantalla principal
# -----------------------------------------------------------------------------
def cerrar_reserva(page, db):
    """Función para cerrar el cuadro de diálogo y volver a la pantalla principal.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    # Cerrar el cuadro de diálogo
    page.dialog.open = False
    # Vaciar los controles de la pantalla
    page.controls.clear()
    # Actualizar la pantalla
    page.update()
    # Volver a la pantalla principal
    main(page, db)


#--------------------------------------------------------------------------------
# Funciones para el manejo de las validaciones de los botones de las vistas
#------------------------------------------------------------------------------

# Función para validar los datos del cliente y enviarlos a la base de datos
# -----------------------------------------------------------------------------
def DatosCliente(page, db, nombre, telefono, email, direccion):
    """Valida los campos del formulario y muestra errores si son incorrectos.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (ft.TextField): El campo de nombre.
        telefono (ft.TextField): El campo de telefono.
        email (ft.TextField): El campo de email.
        direccion (ft.TextField): El campo de direccion.
    
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el Nombre sea correcto
    error_nombre = validar_nombre(nombre.value)
    # Si el Nombre no es correcto, se agrega al listado el error producido
    if error_nombre != None: 
        errores.append(error_nombre)

    # Comprobar que el Telefono sea correcto
    error_telefono = validar_telefono(telefono.value)
    # Si el Telefono no es correcto, se agrega al listado el error producido
    if error_telefono != None:
        errores.append(error_telefono)

    # Comprobar que el Email sea correcto
    error_email = validar_email(email.value)
    # Si el Email no es correcto, se agrega al listado el error producido
    if error_email != None:
        errores.append(error_email)

    # Comprobar que la Direccion sea correcta
    error_direccion = validar_direccion(direccion.value)
    # Si la Direccion no es correcta, se agrega al listado el error producido
    if error_direccion != None:
        errores.append(error_direccion)

    # Si la longitud del listado de errores es mayor a 0
    if len(errores) > 0:
        # Mostrar los errores obtenidos en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Oops!, ha ocurrido un error"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()

    # Si los campos son correctos, insertar los datos del cliente en la base de datos llamado a la funcion en el archivo "Querys.py"
    else:
        page.controls.clear()
        page.update()
        # Funcion de la quinta vista principal del archivo fifth_view.py
        SelecionarMesaHora(page, db)
        # Funcion para insertar los datos en la base de datos del archivo "Querys.py"
        insertar_datos_clientes(page, db, nombre.value, telefono.value, email.value, direccion.value)

def DatosClienteBuscarReservaModificar(page, db, nombre, telefono):
    """Valida los campos del formulario y muestra errores si existen.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (ft.TextField): El campo de nombre.
        telefono (ft.TextField): El campo de telefono.
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el Nombre sea correcto
    error_nombre = validar_nombre(nombre.value)
    # Si el Nombre no es correcto, se agrega al listado el error producido
    if error_nombre != None:        
        errores.append(error_nombre)

    # Comprobar que el Telefono sea correcto
    error_telefono = validar_telefono(telefono.value)
    # Si el Telefono no es correcto, se agrega al listado el error producido
    if error_telefono != None:
        errores.append(error_telefono)

    # Si la longitud del listado de errores es mayor a 0
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Oops!, ha ocurrido un error"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
    
    # Si los campos son correctos
    else:
        # Recoger la lista de reservas del cliente
        reservas_cliente_lista = buscar_reservas(db, nombre.value, telefono.value)

        # Si la longitud de la lista de reservas es 0
        if len(reservas_cliente_lista) == 0:
            # Mostrar un mensaje indicando que no hay reservas asociadas al cliente
            page.dialog = ft.AlertDialog(
                title=ft.Text("Oops!, ha ocurrido un error"),
                content=ft.Text("No se han encontrado reservas asociadas con el cliente ingresado. Por favor, inténtelo de nuevo."),
                actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
            )
            # Abrir el cuadro de diálogo
            page.dialog.open = True
        # Si la longitud de la lista de reservas es mayor a 0
        else:
            # Generar la tabla de reservas con los datos obtenidos
            generar_tabla_reservas_modificar(page, TablaReservas, reservas_cliente_lista)

        # Actualizar la página para reflejar los cambios
        page.update()

def DatosClienteBuscarReservaEliminar(page, db, nombre, telefono):
    """Valida los campos del formulario y muestra errores si existen.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (ft.TextField): El campo de nombre.
        telefono (ft.TextField): El campo de telefono.
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el Nombre sea correcto
    error_nombre = validar_nombre(nombre.value)
    # Si el Nombre no es correcto, se agrega al listado el error producido
    if error_nombre != None:        
        errores.append(error_nombre)

    # Comprobar que el Telefono sea correcto
    error_telefono = validar_telefono(telefono.value)
    # Si el Telefono no es correcto, se agrega al listado el error producido
    if error_telefono != None:
        errores.append(error_telefono)

    # Si la longitud del listado de errores es mayor a 0
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Oops!, ha ocurrido un error"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
    
    # Si los campos son correctos
    else:
        # Recoger la lista de reservas del cliente
        reservas_cliente_lista = buscar_reservas(db, nombre.value, telefono.value)

        # Si la longitud de la lista de reservas es 0
        if len(reservas_cliente_lista) == 0:
            # Mostrar un mensaje indicando que no hay reservas
            page.dialog = ft.AlertDialog(
                title=ft.Text("Oops!, ha ocurrido un error"),
                content=ft.Text("No se han encontrado reservas asociadas con el cliente ingresado. Por favor, inténtelo de nuevo."),
                actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
            )
            # Abrir el cuadro de diálogo
            page.dialog.open = True

        # Si la longitud de la lista de reservas es mayor a 0
        else:
            # Generar la tabla de reservas
            generar_tabla_reservas_eliminar(page, TablaReservas2, reservas_cliente_lista)

        # Actualizar la página para reflejar los cambios
        page.update()


def ReservarMesa(page, db, NumMesa, NumPerson, Hora, Fecha, Notas):
    """Valida los campos del formulario y muestra errores si existen.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        NumMesa (ft.TextField): El campo de NumMesa.
        NumPerson (ft.TextField): El campo de NumPerson.
        Hora (ft.TextField): El campo de Hora.
        Fecha (ft.TextField): El campo de Fecha.
        Notas (ft.TextField): El campo de Notas.
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el NumMesa sea correcto
    error_NumMesa = Validar_num_mesa(NumMesa.value)
    # Si el NumMesa no es correcto, se agrega al listado el error producido
    if error_NumMesa != None:
        errores.append(error_NumMesa)

    # Comprobar que el NumPerson sea correcto
    error_NumPerson = Validar_num_personas(NumPerson.value)
    # Si el NumPerson no es correcto, se agrega al listado el error producido
    if error_NumPerson != None:
        errores.append(error_NumPerson)

    # Comprobar que la Hora sea correcta
    error_Hora = ValidarHora(Hora.value)
    # Si la Hora no es correcta, se agrega al listado el error producido
    if error_Hora != None:
        errores.append(error_Hora)

    # Comprobar que la Fecha sea correcta
    error_Fecha = ValidarFecha(Fecha.value)
    # Si la Fecha no es correcta, se agrega al listado el error producido
    if error_Fecha != None:
        errores.append(error_Fecha)

    # Comprobar que las Notas sean correctas
    error_Notas = ValidarNotas(Notas.value)
    # Si las Notas no son correctas, se agrega al listado el error producido
    if error_Notas != None:
        errores.append(error_Notas)

    # Si la longitud del listado de errores es mayor a 0    
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
    
    # Si los campos son correctos
    else:
        # Insertar los datos en la base de datos y mostrar un cuadro de diálogo
        insertar_datos_reserva(db, NumMesa.value, NumPerson.value, Hora.value, Fecha.value, Notas.value)
        # Mostrar un cuadro de diálogo confirmando la reserva
        page.dialog = ft.AlertDialog(
            title=ft.Text("Reserva Confirmada"),
            content=ft.Text("¡Gracias por reservar mesa en nuestro restaurante! Te esperamos con gratitud y entusiasmo para ofrecerte una experiencia inolvidable. ¡Nos vemos pronto!"),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: cerrar_reserva(page, db))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()

def EliminarReservaCliente(page, db, nombre, telefono, id_fila_eliminar):
    """Valida los campos del formulario y muestra errores si existen.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (ft.TextField): El campo de nombre.
        telefono (ft.TextField): El campo de telefono.
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el Nombre sea correcto
    error_nombre = validar_nombre(nombre.value)
    # Si el Nombre no es correcto, se agrega al listado el error producido
    if error_nombre != None:        
        errores.append(error_nombre)
    
    # Comprobar que el Telefono sea correcto
    error_telefono = validar_telefono(telefono.value)
    # Si el Telefono no es correcto, se agrega al listado el error producido
    if error_telefono != None:
        errores.append(error_telefono)

    # Si la longitud del listado de errores es mayor a 0
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
        return

    # Si no se ha seleccionado una reserva
    if id_fila_eliminar is None:
        # Mostrar un cuadro de diálogo informando de que debe seleccionar una reserva
        page.dialog = ft.AlertDialog(
            title=ft.Text("Seleccione una reserva"),
            content=ft.Text("Por favor, seleccione una reserva para eliminar."),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
    
    # Si se ha seleccionado una reserva
    else:
        # Mostrar un cuadro de diálogo de confirmación
        if id_fila_eliminar is not None:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Desea eliminar la reserva?"),
                content=ft.Text("Esta accion no se puede deshacer."),
                actions=[
                    # Botones de confirmación o cancelación. Si se acepta, se llama a la función EliminarReservaConfirmada y se elimina la reserva, si no, se cierra el cuadro de diálogo
                    ft.TextButton("Aceptar", on_click=lambda e: EliminarReservaConfirmada(page, db, id_fila_eliminar)),
                    ft.TextButton("Cancelar", on_click=lambda e: close_dialog(page))
                    ],
            )
            # Abrir el cuadro de diálogo
            page.dialog.open = True
            # Actualizar la pantalla
            page.update()

def EliminarReservaConfirmada(page, db, id_fila_eliminar):
    """Elimina una reserva de la base de datos mediante su ID y muestra un cuadro de diálogo de confirmación.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        id_fila_eliminar (int): El ID de la reserva a eliminar.
    """
    # Eliminar la reserva          
    EliminarReservaSelecionada(db, id_fila_eliminar )

    # Mostrar confirmación en un cuadro de diálogo
    page.dialog = ft.AlertDialog(
        title=ft.Text("Reserva Eliminada"),
        content=ft.Text("Su reserva ha sido eliminada con exito."),
        actions=[ft.TextButton("Aceptar", on_click=lambda e: cerrar_reserva(page, db))],
    )
    # Abrir el cuadro de diálogo
    page.dialog.open = True
    # Actualizar la pantalla
    page.update()

def IrAModificarReserva(page, db, nombre, telefono, id_fila_eliminar):
    """Valida los campos del formulario y muestra errores si existen.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        nombre (ft.TextField): El campo de nombre.
        telefono (ft.TextField): El campo de telefono.
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el Nombre sea correcto
    error_nombre = validar_nombre(nombre.value)
    # Si el Nombre no es correcto, se agrega al listado el error producido
    if error_nombre != None:        
        errores.append(error_nombre)

    # Comprobar que el Telefono sea correcto
    error_telefono = validar_telefono(telefono.value)
    # Si el Telefono no es correcto, se agrega al listado el error producido
    if error_telefono != None:
        errores.append(error_telefono)

    # Si la longitud del listado de errores es mayor a 0
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
        return
    
    # Si no se ha seleccionado una reserva
    if id_fila_eliminar is None:
        # Mostrar un cuadro de diálogo informando de que debe seleccionar una reserva
        page.dialog = ft.AlertDialog(
            title=ft.Text("Seleccione una reserva"),
            content=ft.Text("Por favor, seleccione una reserva para modificar."),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()

    # Si se ha seleccionado una reserva
    else:
        # Limpiar la pantalla
        page.controls.clear()
        # Actualizar la pantalla
        page.update()
        # Ir a la vista de modificar reserva
        ModificarReserva(page, db, id_fila_eliminar)

def ValidarReserva(page, db, NumMesa, Fecha, Hora, NumPerson, Notas, id_reserva):
    """Valida los campos del formulario y muestra errores si existen.
    
    Args:
        page (ft.Page): La pagina actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
        NumMesa (ft.TextField): El campo de NumMesa.
        Fecha (ft.TextField): El campo de Fecha.    
        Hora (ft.TextField): El campo de Hora.
        NumPerson (ft.TextField): El campo de NumPerson.
        Notas (ft.TextField): El campo de Notas.
        id_reserva (int): El ID de la reserva.
    """
    # Listado de errores producidos trás las validaciones
    errores = []

    # Comprobar que el NumMesa sea correcto
    error_NumMesa = Validar_num_mesa(NumMesa)
    # Si el NumMesa no es correcto, se agrega al listado el error producido
    if error_NumMesa != None:
        errores.append(error_NumMesa)

    # Comprobar que la Fecha sea correcta
    error_Fecha = ValidarFecha(Fecha)
    # Si la Fecha no es correcta, se agrega al listado el error producido
    if error_Fecha != None:
        errores.append(error_Fecha)

    # Comprobar que la Hora sea correcta
    error_Hora = ValidarHora(Hora)
    # Si la Hora no es correcta, se agrega al listado el error producido
    if error_Hora != None:
        errores.append(error_Hora)

    # Comprobar que el NumPerson sea correcto
    error_NumPerson = Validar_num_personas(NumPerson)
    # Si el NumPerson no es correcto, se agrega al listado el error producido
    if error_NumPerson != None:
        errores.append(error_NumPerson)

    # Comprobar que las Notas sean correctas
    error_Notas = ValidarNotas(Notas)
    # Si las Notas no son correctas, se agrega al listado el error producido
    if error_Notas != None:
        errores.append(error_Notas)
    
    # Si la longitud del listado de errores es mayor a 0
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()
    
    # Si la longitud del listado de errores es 0
    else:
        # Guardar la reserva en la base de datos
        GuardarReserva(db, NumMesa, Fecha, Hora, NumPerson, Notas, id_reserva)
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Reserva Modificada"),
            content=ft.Text("¡Su reserva ha sido moficada con exito! Te esperamos con gratitud y entusiasmo para ofrecerte una experiencia inolvidable. ¡Nos vemos pronto!"),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: cerrar_reserva(page, db))],
        )
        # Abrir el cuadro de diálogo
        page.dialog.open = True
        # Actualizar la pantalla
        page.update()