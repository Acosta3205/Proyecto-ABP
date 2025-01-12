import datetime
import locale
import flet as ft

from services.querys import mostrar_mesas
from services.querys import mostrar_nota_mesa


def DatosReserva(page, db, TextMesa, TextNumPersonas, TextHora, TextFecha, TextNota):
    from utils.validators import ReservarMesa
    ReservarMesa(page, db, TextMesa, TextNumPersonas, TextHora, TextFecha, TextNota)

fifth_view_content = []

def SelecionarMesaHora(page: ft.Page, db):
    page.title = "Sabores Unicos - Elegir Mesa y Hora de reserva"
    page.route = "RealizarReserva/ElegirMesaHoraDeReserva"

    # Establece el idioma en español
    locale.setlocale(locale.LC_TIME, 'es_ES')

    # Maneja el cambio de fecha
    def handle_change_date(e):
        TextFecha.value = e.control.value.strftime('%d de %B %Y')
        page.update()
    
    # Maneja el cambio de hora
    def handle_change_time(e):
        TextHora.value = e.control.value.strftime('%H:%M')
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

    # Container para el campo de texto y botón para seleccionar la fecha
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
    
    def back_to_second_view(page: ft.Page, db):
        # Guardar el contenido de la segunda vista
        global fifth_view_content
        fifth_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.second_view import realizar_reserva
        realizar_reserva(page, db)
    
    def back_to_first_view(page: ft.Page, db):
        # Guardar el contenido de la segunda vista
        global second_view_content
        second_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page, db)

    # Header
    ImageHeader = ft.Container(
        content=ft.Image(src="images/banner2.png", fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
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
                                          width=466,
                                          height=79,
                                          on_click=lambda e: back_to_first_view(page, db), 
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=466,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Productos", 
                                          width=466,
                                          height=79,
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=466,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Nosotros", 
                                          width=466,
                                          height=79,
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=466,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton("Contacto", 
                                          width=466,
                                          height=79, 
                                          style=ft.ButtonStyle(bgcolor={"": "#FFC061", ft.ControlState.HOVERED: "black"}, color={"": "black", ft.ControlState.HOVERED: "white"}, side={"": ft.BorderSide(width=0, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="#FFC061")}, shape=ft.RoundedRectangleBorder(radius=0), padding=20, text_style=ft.TextStyle(size=32, weight=ft.FontWeight.W_600))),
                                ],
                            ),
                            padding=0,
                            alignment=ft.alignment.center,
                            width=466,
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
            ],
        ),
        alignment=ft.alignment.center,
        bgcolor="#FFC061",
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

    TextNumPersonas = ft.TextField(
                        label="Numero de personas",
                        hint_text="Introduzca el numero de personas",
                        bgcolor="white",
                        border_color="white",
                        label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                        border=ft.InputBorder.NONE, 
                        filled=True,
                )
    
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
        numMesas = mostrar_mesas(db, TextNumPersonas.value)

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
                            "Confirmar reserva",
                            on_click=lambda e: DatosReserva(page, db, TextMesa, TextNumPersonas, TextHora, TextFecha, TextNota),
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
                            on_click=lambda e: back_to_second_view(page, db),
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
                ft.Text("¡Realiza tu reserva!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text("Introduzca los datos de la reserva:", size=28, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
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

    # Contenedor para la sección de contacto
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
                            width=425,
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
                            width=425, 
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
                            width=425,
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
                            width=425,
                        ),
                    ],
                    alignment=ft.alignment.center,
                    spacing=40,
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text("© 2024 Sabores Únicos. Todos los derechos reservados.", size=14, weight=ft.FontWeight.W_400),
                            alignment=ft.alignment.center,
                            padding=7,
                            width=471 * 4,
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
            ],
        ),
        alignment=ft.alignment.center,
        padding=5,
        bgcolor="#FFC061",
    )

    page.add(
        ImageHeader,
        Header,
        datos_reserva,
        contact_section,
        )
