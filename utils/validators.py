def validar_dni(dni: str):
    """Comprueba que el DNI proporcionado tiene el formato 00000000A"""
    # Solicitar el DNI
    while True:
        # Comprobar que el DNI no este vacío
        if len(dni) == 0:
            print("El DNI no puede estar vacío. Por favor, introduzca de nuevo el DNI.")
        # Comprobar que el DNI tenga una longitud de 9 caracteres
        elif len(dni) != 9:
            print("El DNI debe tener una longitud de 9 caracteres. Por favor, introduzca de nuevo el DNI.")
        # Comprobar que el DNI tenga el formato 00000000A
        elif dni[0:8].isnumeric() == False or dni[8].isalpha() == False:
            print("El DNI debe tener el formato 00000000A. Por favor, introduzca de nuevo el DNI.")
        # Si el DNI es correcto, salir del bucle
        else:
            return dni
        # Solicitar el DNI de nuevo
        dni = input("Introduzca el DNI del nuevo cliente: ")

def validar_Nombre(nombre: str):
    """Comprueba que el nombre proporcionado tiene entre 1 y 20 caracteres y que no sean dígitos"""
    while True:
        # Comprobar que el nombre tenga entre 1 y 20 caracteres
        if not (0 < len(nombre) <= 20):
            print('El nombre debe tener entre 1 y 20 caracteres')
        # Comprobar que el nombre no contenga dígitos
        elif not nombre.isalpha():
            print('El nombre no puede contener dígitos')
        # Si el nombre es correcto, sale del bucle
        else:
            return nombre
        # Solicitar el nombre de nuevo
        nombre = input('Introduce el nombre del empleado: ')                               


def validar_telefono(telefono: int):
    """Comprueba que el teléfono proporcionado tiene 9 digitos"""
    while True:
        # Comprobar que el telefono tenga 9 caracteres
        if not len(telefono) == 9:
            print('El telefono tiene que tener 9 caracteres')
        # Comprobar que el telefono tiene que ser un numero
        elif not telefono.isdigit():
            print('El telefono tiene que ser un numero')
        # Si el teléfono es correcto, sale del bucle
        else:
            return telefono
        # Solicitar el teléfono de nuevo
        telefono = input('Introduce el telefono del cliente: ')

def validar_email(email: str):
    """Comprueba que el email proporcionado tiene el formato correo@dominio.com"""
    # Comprobar que el email no este vacío
    if len(email) == 0:
        print("El email no puede estar vacío. Por favor, introduzca de nuevo el email.")
    # Comprobar que el email tenga un @ y un .
    elif email.count("@") != 1 or email.count(".") != 1:
        print("El email debe tener un @ y un .")
    # Comprobar que el email tenga el formato correo@dominio.
    elif len(email.split("@")[0]) == 0 or len(email.split("@")[1]) == 0:
        print("El email debe tener el formato correo@dominio.") 
    # Comprobar que el email tenga el formato correo@dominio.com
    elif len(email.split("@")[1].split(".")[0]) == 0 or len(email.split("@")[1].split(".")[1]) == 0:
        print("El email debe tener el formato correo@dominio.com")
    # Si el email es correcto, sale del bucle
    else:
        return email
    
def validar_direccion(direccion: str):
    """Comprueba que la direccion proporcionada no este vacio"""
    # Comprobar que la direccion no este vacia
    if len(direccion) == 0:
        print("La direccion no puede estar vacia. Por favor, introduzca de nuevo la direccion.")
    # Si la direccion es correcta, sale del bucle
    else:
        return direccion
    # Solicitar la direccion de nuevo
    direccion = input("Introduzca la direccion del nuevo cliente: ")
    
    
def validarFecha(fecha: str):
    # Función para validar fechas en formato YYYY-MM-DD
    while True:
        # Comprobar que la fecha tenga 10 caracteres
        if not len(fecha) == 10:
            print("La longitud de la fecha debe ser de 10 caracteres")
        # Comprobar que la fecha tenga el formato YYYY-MM-DD
        elif not (fecha[4] == '-' and fecha[7] == '-'):
            print("El formato de fecha que has introducido es incorrecto (YYYY-MM-DD)")
        # Comprobar que sean números
        elif not (fecha[0:4].isdigit() and fecha[5:7].isdigit() and fecha[8:10].isdigit()):
            print("Formato de fecha incorrecto, debe ser de tipo YYYY-MM-DD")
        # Comprobar que el año esté dentro del rango aceptado
        elif not (1900 <= int(fecha[0:4]) <= 2024):
            print("El año debe estar entre 1900 y 2024")
        # Comprobar que el mes no sea negativo o superior a 12
        elif not (1 <= int(fecha[5:7]) <= 12):
            print("Los meses de un año no pueden ser negativos o superiores a 12")
        # Comprobar que el día no sea negativo o superior a 31
        elif not (1 <= int(fecha[8:10]) <= 31):
            print("Los días de un mes no pueden ser negativos o superiores a 31")
        else:
            return fecha  # Si es válida, retornar la fecha
        # Si alguna verificación falla, pedir una nueva fecha
        fecha = input("Vuelve a ingresar la fecha (YYYY-MM-DD): ")