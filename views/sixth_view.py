#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------
import datetime
import locale
import flet as ft

#-------------------------------------------------------
# Importación de las funciones necesarias
#-------------------------------------------------------

from services.querys import mostrar_mesas
from services.querys import mostrar_nota_mesa
from services.querys import CargarDatosReserva


def ValidarReserva(page, db, TextMesa, TextFecha, TextHora, TextNumPersonas, TextNota, id_reserva):
    from utils.validators import ValidarReserva
    ValidarReserva(page, db, TextMesa.value, TextFecha.value, TextHora.value, TextNumPersonas.value, TextNota.value, id_reserva)

# Variable global para almacenar el contenido de las vista
sixth_view_content = []

def ModificarReserva(page: ft.Page, db, id_reserva):
    """Maneja el comportamiento de la sexta vista del programa.
    
    Args:
        page (ft.Page): La página actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    page.title = "Sabores Unicos - Modificar datos de la reserva"
    page.route = "ModificarReserva/ModificarDatosReserva"

    # Recuperar los datos de la reserva pertenecientes al ID recibido
    reserva = CargarDatosReserva(page, db, id_reserva)

    # Establece el idioma en español
    locale.setlocale(locale.LC_TIME, 'es_ES')

    # Función para volver a la vista anterior
    def back_to_third_view(page: ft.Page, db):
        """Vacía el contenido de la página actual y carga el contenido de la tercera vista.
        
        Args:
            page (ft.Page): La página actual.
            db (pymongo.database.Database): La base de datos de MongoDB.
        """
        # Guardar el contenido de la segunda vista
        global sixth_view_content
        sixth_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.third_view import editar_reserva, TablaReservas
        TablaReservas.rows.clear()
        editar_reserva(page, db)

    
    # Funciones para manejar la navegación entre las vistas
    
    def back_to_first_view(page: ft.Page, db):
        """Vacía el contenido de la página actual y carga el contenido de la primera vista.
        
        Args:
            page (ft.Page): La página actual.
            db (pymongo.database.Database): La base de datos de MongoDB.
        """
        # Guardar el contenido de la segunda vista
        global second_view_content
        second_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page, db)

    # Funciones para manejar el formato de la fecha y hora

    # Maneja el cambio de fecha
    def handle_change_date(e):
        """"Formatea la fecha como día de mes de año (02 de Mayo de 2024).
        
        Args:
            e (ft.Event): El evento de edición de los campos de texto.
        """
        TextFecha.value = e.control.value.strftime('%d de %B %Y')
        activar_num_personas()
        page.update()
    
    # Maneja el cambio de hora
    def handle_change_time(e):
        """Formatea la hora como HH:MM (19:25).
        
        Args:
            e (ft.Event): El evento de edición de los campos de texto.
        """
        TextHora.value = e.control.value.strftime('%H:%M')
        activar_num_personas()
        page.update()
    
    # Campo de texto para la fecha
    TextFecha = ft.TextField(
                            label="Fecha",
                            hint_text="Introduzca la fecha",
                            bgcolor="white",
                            border_color="white",
                            label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                            border=ft.InputBorder.NONE,
                            filled=True,
                            read_only=True,
                            width=325 * 4,
                        )
    
    # Asociar el valor del campo de texto con el valor de la fecha obtenido de la reserva consultada    
    TextFecha.value = reserva["fecha"]
    
    # Container para el campo de texto y botón para seleccionar la fecha
    fecha_container = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        TextFecha,
                        ft.ElevatedButton(
                            "Seleccionar Fecha",
                            icon=ft.icons.CALENDAR_MONTH,
                            width=225,
                            height=48,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0),
                            ),
                            on_click=lambda e: page.open(
                                ft.DatePicker(
                                    first_date=datetime.date.today(),
                                    last_date=datetime.datetime(year=2025, month=2, day=28),
                                    on_change=handle_change_date,
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )
    
    # Campo de texto para la hora
    TextHora = ft.TextField(
                    label="Hora",
                    hint_text="Introduzca la hora",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                    read_only=True,
                    width=325 * 4,
                )
    
    # Asociar el valor del campo de texto con el valor de la hora obtenido de la reserva consultada    
    TextHora.value = reserva["hora"]

    # Container para el campo de texto y botón para seleccionar la hora
    hora_container = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        TextHora,
                        ft.ElevatedButton(
                            "Seleccionar Hora",
                            icon=ft.icons.ACCESS_TIME,
                            width=225,
                            height=48,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0),
                            ),
                            on_click=lambda e: page.open(
                                ft.TimePicker(
                                    on_change=handle_change_time,
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # -------------------------------------------------------------
    # Funciones para manejar los cambios de los campos de texto de Numero de personas y Mesa
    # ------------------------------------------------------------

    # Función para activar el campo NumPersonas
    def activar_num_personas():
        # Vaciar el listado de mesas
        TextMesa.options.clear()

        # Vaciar el campo NumPersonas
        TextNumPersonas.value = ""  # Vaciar el campo de texto
        page.update()  # Actualizar la interfaz

        if TextFecha.value != "" and TextHora.value != "":
            TextNumPersonas.read_only = False
        else:
            TextNumPersonas.read_only = True
        
        page.update()

    # Header
    ImageHeader = ft.Container(
        content=ft.Image(src="images/banner2.png", fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
        width=1920,
    )

    # Contenedor para la sección de contacto
    Header = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Inicio", 
                                          width=472,
                                          height=79,
                                          on_click=lambda e: back_to_first_view(page, db), 
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=472,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Productos", 
                                          width=472,
                                          height=79,
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=472,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Nosotros", 
                                          width=472,
                                          height=79,
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=472,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Contacto", 
                                          width=472,
                                          height=79, 
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=472,
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
            ],
        ),
        alignment=ft.alignment.center,
        bgcolor="#FFC061",
        width=1920,
        height=79, 
    )

    TextMesa = ft.Dropdown(
                    label="Mesa",
                    hint_text="Seleciona la mesa",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                    options=[
                    ],
                )
    
    TextMesa.options.append(ft.dropdown.Option(reserva["id_mesa"]))

    # Establecer el valor seleccionado automáticamente
    TextMesa.value = reserva["id_mesa"]

    TextNumPersonas = ft.TextField(
                        label="Numero de personas",
                        hint_text="Introduzca el numero de personas",
                        bgcolor="white",
                        border_color="white",
                        label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                        border=ft.InputBorder.NONE, 
                        filled=True,
                )
    
    TextNumPersonas.value = reserva["num_personas"]
    
    TextNota = ft.TextField(
                    label="Nota",
                    hint_text="Ubicación de la mesa",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE, 
                    filled=True,
                    read_only=True,
                )
    
    TextNota.value = reserva["notas"]
    
    def funcionNota(e):
        """Si hay selecionada una mesa se muestra en el campo nota la ubicación de la mesa"""
        if TextMesa.value:
            # Obtener la nota de la mesa
            ubicacion = mostrar_nota_mesa(db, TextMesa.value)
            
            # Verificar si se obtuvo una ubicación válida
            if ubicacion:
                TextNota.value = "Ubicación de la mesa: " + ubicacion
            else:
                TextNota.value = "Ubicación de la mesa no encontrada"

        TextNota.update()
    
    def añadirMesasListado(e):
        """Recibe la lista de mesas adecuadas al número de personas y las agrega a la lista desplegable de mesas"""
        numMesas = mostrar_mesas(db, TextNumPersonas.value, TextFecha.value, TextHora.value)

        # Vaciar el campo de nota
        TextNota.value = ""

        # Actualizar el campo de nota
        TextNota.update()

        # Vaciar el listado de mesas
        TextMesa.options.clear()

        # Vaciar el campo de mesa
        TextMesa.value = ""

        # Actualizar el listado de mesas
        TextMesa.update()

        # Añadir las nuevas mesas
        for mesa in numMesas:
            TextMesa.options.append(ft.dropdown.Option(mesa))

        # Actualizar el listado de mesas
        TextMesa.update()

    TextNumPersonas.on_change = añadirMesasListado
    TextMesa.on_change = funcionNota
    
    BotonConfirmar = ft.ElevatedButton(
                            "Guardar reserva",
                            on_click=lambda e: ValidarReserva(page, db, TextMesa,TextFecha, TextHora, TextNumPersonas, TextNota, id_reserva),
                            # on_click=lambda e: back_to_first_view(page),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )
    
    BotonVolver = ft.ElevatedButton(
                            "Volver",
                            on_click=lambda e: back_to_third_view(page, db),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )

    # Welcome Section
    datos_reserva = ft.Container(
        width=315 * 5,
        content=ft.Column(
            [
                ft.Text("Modifica tu reserva!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text("Introduzca los nuevos datos de la reserva:", size=28, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                TextMesa,
                fecha_container,
                hora_container,
                TextNumPersonas,
                TextNota,
                ft.Row(
                    [
                        BotonConfirmar,
                        BotonVolver,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=10,
                ),        
            ],
            spacing=15,
        ),
        padding=20,
    )

    #---------------------------------------------------------------------
    # Contenedor para la sección de datos de contacto del restaurante
    #---------------------------------------------------------------------

    contact_section = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Contáctanos", size=24, weight=ft.FontWeight.W_600),
                                    ft.Text("📍 Dirección: Calle Sabores, 123, Ciudad Gourmet", size=16),
                                    ft.Text("📞 Teléfono: +34 623 456 789", size=16),
                                    ft.Text("📧 Correo: contacto@saboresunicos.com", size=16),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            width=480,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Ayuda", size=24, weight=ft.FontWeight.W_600),
                                    ft.Text("🥖 Alergenos", size=16),
                                    ft.Text("🎁 Información de promociones", size=16),
                                    ft.Text("🍽️ Información nutricional", size=16),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            width=480, 
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Datos de la empresa", size=24, weight=ft.FontWeight.W_600),
                                    ft.Text("🗒️ Nombre: Sabores Únicos S.A.", size=16),
                                    ft.Text("📅 Fundación: 2010", size=16),
                                    ft.Text("🌐 Web: www.saboresunicos.com", size=16),
                                ],
                            ),
                            alignment=ft.alignment.center,
                            width=480,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Términos y condiciones", size=24, weight=ft.FontWeight.W_600),
                                    ft.Text("🔗 Política de privacidad", size=16),
                                    ft.Text("📃 Términos de uso", size=16),
                                    ft.Text("🔒 Seguridad", size=16),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            width=480,
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text("© 2024 Sabores Únicos. Todos los derechos reservados.", size=14, weight=ft.FontWeight.W_400),
                            alignment=ft.alignment.center,
                            width=1920,
                            bgcolor="#b8b8b8",
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
            ],
        ),
        alignment=ft.alignment.center,
        bgcolor="#FFC061",
        width=1920,
    )


    # Agregar los contenedores a la página
    page.add(
        ImageHeader,
        Header,
        datos_reserva,
        contact_section,
    )
    
