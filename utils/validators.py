import flet as ft
from views.fifth_view import SelecionarMesaHora
from views.main_view import main
from services.crud_operations import insertar_datos_clientes, insertar_datos_reserva

def validar_nombre(nombre: str):
    """Comprueba que el nombre proporcionado tiene entre 1 y 20 caracteres y que no sean dígitos"""
    while True:
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
        return "Debe seleccionar una mesa."
    else:
        return None
    
def Validar_num_personas(NumPerson: int):
    """Comprobar que el campo solo contenga numeros"""
    if not NumPerson.isdigit():
        return "Numero de personas debe ser solo números válidos."
    elif NumPerson == "":
        return "Numero de personas no puede estar vacio"
    else:
        return None
    
def ValidarHora(Hora: str):
    """"Comprobar que la hora esté en el rango de 8:00 a 20:00"""
    if Hora == "":
        return "El campo de hora no puede estar vacio"
    elif int(Hora.split(":")[0]) < 8 or int(Hora.split(":")[0]) > 20:
        return "La hora debe estar entre las 8:00 y las 20:00"
    else:
        return None
    
def ValidarFecha(Fecha: str):
    """"Comprobar que la fecha no este vacia"""
    if Fecha == "":
        return "El campo de fecha no puede estar vacio"
    else:
        return None
    
def ValidarNotas(Notas: str):
    """"Comprobar que la nota no este vacia"""
    if Notas == "":
        return "El campo de notas no puede estar vacio. Debes selecionar una mesa"
    else:
        return None

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
            title=ft.Text("Errores de Validación"),
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
    
    def close_dialog(page):
        page.dialog.open = False
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

    
    def close_dialog(page):
        page.dialog.open = False
        page.update()

    def cerrar_reserva(page, db):
        page.dialog.open = False
        page.controls.clear()
        page.update()
        main(page, db)
