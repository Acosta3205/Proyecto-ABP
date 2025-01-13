#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

import flet as ft

#-------------------------------------------------------
# Importación de las funciones necesarias
#-------------------------------------------------------

from utils.validators import DatosCliente

# Variable global para almacenar el contenido de las vista
second_view_content = []

# -------------------------------------------------------
# Funcion principal del programa
# -------------------------------------------------------

def realizar_reserva(page: ft.Page, db):
    page.title = "Sabores Únicos - Realizar reserva"
    page.route = "/RealizarReserva"
    
    #-------------------------------------------------------
    # Funciones para manejar la navegacion entre las vistas
    #-------------------------------------------------------
   
    def back_to_first_view(page: ft.Page, db):
        """Vacía el contenido de la página actual y carga el contenido de la primera vista."""
        # Guardar el contenido de la segunda vista
        global second_view_content
        second_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page, db)
    
    #-------------------------------------------------------
    # Encabezado
    #------------------------------------------------------- 

    ImageHeader = ft.Container(
        content=ft.Image(src="images/banner2.png", fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
        width=1920,
    )

    #-------------------------------------------------------
    # Contenedor para la sección de contacto
    #-------------------------------------------------------

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
                            height=79
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
                            height=79
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
                            height=79
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
                            height=79
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

    #-------------------------------------------------------
    # Campos de texto para el formulario
    #-------------------------------------------------------

    # Campo de texto para el nombre
    TextNombre = ft.TextField(
                    label="Nombre",
                    hint_text="Introduzca su nombre",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )
    # Campo de texto para el telefono
    TextTelefono = ft.TextField(
                    label="Telefono",
                    hint_text="Introduzca su telefono",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )
    # Campo de texto para la dirección
    TextDireccion = ft.TextField(
                    label="Dirección",
                    hint_text="Introduzca su direción",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE, 
                    filled=True,
                )
    # Campo de texto para el correo
    TextEmail = ft.TextField(
                    label="Email",
                    hint_text="Introduzca su correo",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )
    
    #-------------------------------------------------------
    # Botones para el formulario
    #-------------------------------------------------------

    # Botón para avanzar al formulario para seleccionar mesa y hora
    BotonMesa = ft.ElevatedButton(
                            "Selecionar Mesa y Hora",
                            on_click=lambda e: DatosCliente(page, db, TextNombre, TextTelefono, TextEmail, TextDireccion),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )
    
    # Botón para volver a la vista anterior
    BotonVolver = ft.ElevatedButton(
                            "Volver",
                            on_click=lambda e: back_to_first_view(page, db),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )
    
    #--------------------------------------------------------------------
    # Contenedor para la sección de inserción de los datos de contacto
    #--------------------------------------------------------------------
    
    realizar_reserva = ft.Container(
        width=315 * 5,
        content=ft.Column(
            [
                ft.Text("¡Realiza tu reserva!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text("Por favor, introduzca sus datos de contacto:", size=28, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                TextNombre,
                TextTelefono,
                TextEmail,
                TextDireccion,
                ft.Row(
                    [
                        BotonMesa,
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

    #---------------------------------------------------------------
    # Agregar a la página los contenedores que forman la sección
    #---------------------------------------------------------------

    page.add(
        ImageHeader,
        Header,
        realizar_reserva,
        contact_section,
        )
        
    