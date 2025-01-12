import flet as ft
from views.fifth_view import SelecionarMesaHora
from views.main_view import main
from views.third_view import TablaReservas, generar_tabla_reservas
from views.four_view import TablaReservas2
from views.sixth_view import ModificarReserva


from services.crud_operations import insertar_datos_clientes, insertar_datos_reserva , GuardarReserva

from services.querys import buscar_reservas, EliminarReservaSelecionada

def validar_nombre(nombre: str):
    """Comprueba que el nombre proporcionado tiene entre 1 y 20 caracteres y que no sean dígitos"""
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

def validar_telefono(telefono: int):
    """Comprueba que el teléfono proporcionado tiene 9 digitos"""
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

def validar_email(email: str):
    """Comprueba que el email proporcionado tiene el formato correo@dominio.com"""
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
    
def validar_direccion(direccion: str):
    """Comprueba que la direccion proporcionada no este vacio"""
    # Comprobar que la direccion no este vacia
    if len(direccion) == 0:
        return "La direccion no puede estar vacia."
    # Si la direccion es correcta, sale del bucle
    else:
        return None

def Validar_num_mesa(NumMesa: int):
    """Comprobar que el campo solo contenga numeros"""
    if not NumMesa:
        return "Debe seleccionar una mesa para la reserva."
    else:
        return None
    
def Validar_num_personas(NumPerson):
    """Comprobar que el campo solo contenga numeros"""
    if NumPerson == "":
        return "Introduzca el numero de personas para la reserva"
    elif not NumPerson.isdigit():
        return "El campo de personas solo puede contener numeros."
    else:
        return None
    
def ValidarHora(Hora: str):
    """"Comprobar que la hora esté en el rango de 8:00 a 20:00"""
    if Hora == "":
        return "Introduzca una hora para la reserva"
    elif int(Hora.split(":")[0]) < 8 or int(Hora.split(":")[0]) > 20:
        return "El horario de reservas es de 8:00 a 20:00"
    else:
        return None
    
def ValidarFecha(Fecha: str):
    """"Comprobar que la fecha no este vacia"""
    if Fecha == "":
        return "Introduzca una fecha para la reserva"
    else:
        return None
    
def ValidarNotas(Notas: str):
    """"Comprobar que la nota no este vacia"""
    if Notas == "":
        return "El campo de notas no puede estar vacio. Debes selecionar una mesa"
    else:
        return None
    
def close_dialog(page):
        page.dialog.open = False
        page.update()

def cerrar_reserva(page, db):
    page.dialog.open = False
    page.controls.clear()
    page.update()
    main(page, db)

def DatosCliente(page, db, nombre, telefono, email, direccion):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    error_nombre = validar_nombre(nombre.value)
    if error_nombre != None:        
        errores.append(error_nombre)

    error_telefono = validar_telefono(telefono.value)
    if error_telefono != None:
        errores.append(error_telefono)

    error_email = validar_email(email.value)
    if error_email != None:
        errores.append(error_email)

    error_direccion = validar_direccion(direccion.value)
    if error_direccion != None:
        errores.append(error_direccion)

    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Oops!, ha ocurrido un error"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        page.controls.clear()
        page.update()
        SelecionarMesaHora(page, db)
        insertar_datos_clientes(page, db, nombre.value, telefono.value, email.value, direccion.value)

def DatosClienteBuscarReservaModificar(page, db, nombre, telefono):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    error_nombre = validar_nombre(nombre.value)
    if error_nombre != None:        
        errores.append(error_nombre)

    error_telefono = validar_telefono(telefono.value)
    if error_telefono != None:
        errores.append(error_telefono)

    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Oops!, ha ocurrido un error"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        # Recoger la lista de reservas del cliente
        reservas_cliente_lista = buscar_reservas(db, nombre.value, telefono.value)
    
        # Generar la tabla de reservas
        generar_tabla_reservas(page, TablaReservas, reservas_cliente_lista)

        # Actualizar la página para reflejar los cambios
        page.update()

def DatosClienteBuscarReservaEliminar(page, db, nombre, telefono):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    error_nombre = validar_nombre(nombre.value)
    if error_nombre != None:        
        errores.append(error_nombre)

    error_telefono = validar_telefono(telefono.value)
    if error_telefono != None:
        errores.append(error_telefono)

    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Oops!, ha ocurrido un error"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        # Recoger la lista de reservas del cliente
        reservas_cliente_lista = buscar_reservas(db, nombre.value, telefono.value)
    
        # Generar la tabla de reservas
        generar_tabla_reservas(page, TablaReservas2, reservas_cliente_lista)

        # Actualizar la página para reflejar los cambios
        page.update()


def ReservarMesa(page, db, NumMesa, NumPerson, Hora, Fecha, Notas):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    error_NumMesa = Validar_num_mesa(NumMesa.value)
    if error_NumMesa != None:
        errores.append(error_NumMesa)
    
    error_NumPerson = Validar_num_personas(NumPerson.value)
    if error_NumPerson != None:
        errores.append(error_NumPerson)

    error_Hora = ValidarHora(Hora.value)
    if error_Hora != None:
        errores.append(error_Hora)

    error_Fecha = ValidarFecha(Fecha.value)
    if error_Fecha != None:
        errores.append(error_Fecha)

    error_Notas = ValidarNotas(Notas.value)
    if error_Notas != None:
        errores.append(error_Notas)
        
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        insertar_datos_reserva(db, NumMesa.value, NumPerson.value, Hora.value, Fecha.value, Notas.value)
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Reserva Confirmada"),
            content=ft.Text("¡Gracias por reservar mesa en nuestro restaurante! Te esperamos con gratitud y entusiasmo para ofrecerte una experiencia inolvidable. ¡Nos vemos pronto!"),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: cerrar_reserva(page, db))],
        )
        page.dialog.open = True
        page.update()

def EliminarReservaCliente(page, db, nombre, telefono, id_fila_eliminar):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    error_nombre = validar_nombre(nombre.value)
    if error_nombre != None:        
        errores.append(error_nombre)

    error_telefono = validar_telefono(telefono.value)
    if error_telefono != None:
        errores.append(error_telefono)

    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
        return


    print("Validators: ", id_fila_eliminar)
    if id_fila_eliminar is None:
        page.dialog = ft.AlertDialog(
            title=ft.Text("Seleccione una reserva"),
            content=ft.Text("Por favor, seleccione una reserva para eliminar."),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        if id_fila_eliminar is not None:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Desea eliminar la reserva?"),
                content=ft.Text("Esta accion no se puede deshacer."),
                actions=[
                    ft.TextButton("Aceptar", on_click=lambda e: EliminarReservaConfirmada(page, db, id_fila_eliminar)),
                    ft.TextButton("Cancelar", on_click=lambda e: close_dialog(page))
                    ],
            )
            page.dialog.open = True
            page.update()

def EliminarReservaConfirmada(page, db, id_fila_eliminar):

    # Eliminar la reserva          
    EliminarReservaSelecionada(db, id_fila_eliminar )

    # Mostrar confirmación en un cuadro de diálogo
    page.dialog = ft.AlertDialog(
        title=ft.Text("Reserva Eliminada"),
        content=ft.Text("Su reserva ha sido eliminada con exito."),
        actions=[ft.TextButton("Aceptar", on_click=lambda e: cerrar_reserva(page, db))],
    )
    page.dialog.open = True
    page.update()

def IrAModificarReserva(page, db, nombre, telefono, id_fila_eliminar):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    error_nombre = validar_nombre(nombre.value)
    if error_nombre != None:        
        errores.append(error_nombre)

    error_telefono = validar_telefono(telefono.value)
    if error_telefono != None:
        errores.append(error_telefono)

    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
        return
    
    print("ID Fila Recogida: ", id_fila_eliminar)

    if id_fila_eliminar is None:
        page.dialog = ft.AlertDialog(
            title=ft.Text("Seleccione una reserva"),
            content=ft.Text("Por favor, seleccione una reserva para modificar."),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        page.controls.clear()
        page.update()
        ModificarReserva(page, db, id_fila_eliminar)

def ValidarReserva(page, db, NumMesa, Fecha, Hora, NumPerson, Notas, id_reserva):
    """Valida los campos del formulario y muestra errores si existen."""
    errores = []

    print(NumPerson)

    error_NumMesa = Validar_num_mesa(NumMesa)
    if error_NumMesa != None:
        errores.append(error_NumMesa)
    
    error_NumPerson = Validar_num_personas(NumPerson)
    if error_NumPerson != None:
        errores.append(error_NumPerson)

    error_Hora = ValidarHora(Hora)
    if error_Hora != None:
        errores.append(error_Hora)

    error_Fecha = ValidarFecha(Fecha)
    if error_Fecha != None:
        errores.append(error_Fecha)

    error_Notas = ValidarNotas(Notas)
    if error_Notas != None:
        errores.append(error_Notas)
        
    if len(errores) > 0:
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Errores de Validación"),
            content=ft.Text("\n".join(errores)),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: close_dialog(page))],
        )
        page.dialog.open = True
        page.update()
    else:
        GuardarReserva(db, NumMesa, Fecha, Hora, NumPerson, Notas, id_reserva)
        # Mostrar errores en un cuadro de diálogo
        page.dialog = ft.AlertDialog(
            title=ft.Text("Reserva Modificada"),
            content=ft.Text("¡Su reserva ha sido moficada con exito! Te esperamos con gratitud y entusiasmo para ofrecerte una experiencia inolvidable. ¡Nos vemos pronto!"),
            actions=[ft.TextButton("Aceptar", on_click=lambda e: cerrar_reserva(page, db))],
        )
        page.dialog.open = True
        page.update()