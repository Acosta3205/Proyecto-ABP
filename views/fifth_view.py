# --------------------------------
# Importar librerias necesarias
# --------------------------------
import datetime
import locale
import flet as ft

# ---------------------------------------------------
# Importar consultas del archivo querys nesesarias
# ---------------------------------------------------

from services.querys import mostrar_mesas
from services.querys import mostrar_nota_mesa

# ---------------------------------------------------
# Importar funciones para las validaciones de los campos
# ---------------------------------------------------

def DatosReserva(page, db, TextMesa, TextNumPersonas, TextHora, TextFecha, TextNota):
    from utils.validators import ReservarMesa
    ReservarMesa(page, db, TextMesa, TextNumPersonas, TextHora, TextFecha, TextNota)

# Variable global para almacenar el contenido de las vista
fifth_view_content = []

# -------------------------------------------------------
# Funcion principal del programa
# -------------------------------------------------------

def SelecionarMesaHora(page: ft.Page, db):
    """Maneja el comportamiento de la quinta vista del programa.
    
    Args:
        page (ft.Page): La página actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    page.title = "Sabores Unicos - Elegir Mesa y Hora de reserva"
    page.route = "RealizarReserva/ElegirMesaHoraDeReserva"

    # Establece el idioma en español
    locale.setlocale(locale.LC_TIME, 'es_ES')

    # -------------------------------------------------------
    # Funciones para manejar la navegacion entre las vistas
    # -------------------------------------------------------

    def back_to_second_view(page: ft.Page, db):
        """Vacía el contenido de la página actual y carga el contenido de la segunda vista.
        
        Args:
            page (ft.Page): La página actual.
            db (pymongo.database.Database): La base de datos de MongoDB.
        """
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
    
    # --------------------------------------------------------------------------
    # Funciones para manejar el desplegable de listas de mesas disponibles
    # ---------------------------------------------------------------------------

    # Función para mostrar la ubicación de la mesa
    # -----------------------------------------------
    def funcionNota(e):
        """Si hay selecionada una mesa se muestra en el campo nota la ubicación de la mesa.
        
        Args:
            e (ft.Event): El evento de edición de los campos de texto.
        """
        if TextMesa.value:
            # Obtener la nota de la mesa
            ubicacion = mostrar_nota_mesa(db, TextMesa.value)
            
            # Verificar si se obtuvo una ubicación válida
            if ubicacion:
                TextNota.value = "Ubicación de la mesa: " + ubicacion
            else:
                TextNota.value = "Ubicación de la mesa no encontrada"

        TextNota.update()
    
    # Función para anadir las mesas adecuadas al número de personas
    # ----------------------------------------------------------------
    def añadirMesasListado(e):
        """Recibe la lista de mesas adecuadas al número de personas y las agrega a la lista desplegable de mesas
        
        Args:
            e (ft.Event): El evento de edición de los campos de texto.
        """
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
    
    # -------------------------------------------------------
    # Funciones para manejar los cambios de fecha y hora
    # -------------------------------------------------------

    # Maneja el cambio de fecha
    # ----------------------------
    def handle_change_date(e):
        """Formatea la fecha como día de mes de año (02 de Mayo de 2024).
        
        Args:
            e (ft.Event): El evento de edición de los campos de texto.
        """
        TextFecha.value = e.control.value.strftime('%d de %B %Y')
        page.update()
    
    # Maneja el cambio de hora
    # ----------------------------
    def handle_change_time(e):
        """Formatea la hora como HH:MM (19:25).
        
        Args:
            e (ft.Event): El evento de edición de los campos de texto.
        """
        TextHora.value = e.control.value.strftime('%H:%M')
        page.update()

    # -------------------------------------------------------------------------
    # TextEdit para el manejo de datos de los clientes en la base de datos
    # --------------------------------------------------------------------------

    # Campo de texto para la mesa
    # -------------------------------
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

    # Campo de texto para la fecha
    # -------------------------------
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
    
    # Campo de texto para la hora
    # -------------------------------
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

    
    # Campo de texto para el numero de personas
    # --------------------------------------------
    TextNumPersonas = ft.TextField(
                        label="Numero de personas",
                        hint_text="Introduzca el numero de personas",
                        bgcolor="white",
                        border_color="white",
                        label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                        border=ft.InputBorder.NONE, 
                        filled=True,
                )
    
    # Campo de texto para la nota
    # -------------------------------
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
    
    # -------------------------------------------------------------
    # Funciones para manejar los cambios de los campos de texto de Numero de personas y Mesa
    # ------------------------------------------------------------
    TextNumPersonas.on_change = añadirMesasListado
    TextMesa.on_change = funcionNota
    
    # -------------------------------------------------------------------------
    # Button para el manejo de los datos de reserva y navegacion de vistas
    # --------------------------------------------------------------------------    
    
    # Boton para confirmar la reserva
    # -----------------------------------
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
    
    # Boton para volver a la segunda vista
    # ----------------------------------------
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
    
    # -------------------------------------------------------------------------
    # Manejar los botones de selecion de los campos de fecha y hora 
    # --------------------------------------------------------------------------

    # Container para el campo de texto y botón para seleccionar la fecha
    # -------------------------------------------------------------------------
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

    # Container para el campo de texto y botón para seleccionar la fecha
    # -------------------------------------------------------------------------
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

    # -------------------------------------------------------
    # Variables globales del la pagina del programa
    # -------------------------------------------------------

    # Imagen de cabecera
    # ---------------------
    ImageHeader = ft.Container(
        content=ft.Image(src="images/banner2.png", fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
        width=1920,
    )

    # Contenedor de botones de navegación del menu principal
    # -----------------------------------------------------------
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

    # Contenedor para la sección de reserva
    # ------------------------------------------
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
    #-------------------------------------------------------
    # Agregar los contenedores a la pantalla
    #-------------------------------------------------------
    page.add(
        ImageHeader,
        Header,
        datos_reserva,
        contact_section,
        )
