import flet as ft
import datetime

four_view_content = []

def EliminarReservaCliente(page, db, TextNombre, TextTelefono):
    from utils.validators import EliminarReservaCliente
    EliminarReservaCliente(page, db, TextNombre, TextTelefono)

def eliminar_reserva(page: ft.Page, db):
    page.title = "Fourth View"
    page.add(ft.Text("Fourth View"))

    # Botón de "volver" que nos regresa a la primera vista
    back_button = ft.ElevatedButton("Back", on_click=lambda e: back_to_first_view(page))
    page.add(back_button)

    def back_to_first_view(page: ft.Page, db):
        # Guardar el contenido de la segunda vista
        global four_view_content
        four_view_content = page.controls[:]

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

    TextNombre = ft.TextField(
                    label="Nombre",
                    hint_text="Introduzca su nombre",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )
    TextTelefono = ft.TextField(
                    label="Telefono",
                    hint_text="Introduzca su telefono",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )
    
    BotonEditar = ft.ElevatedButton(
                            "Eliminar reserva",
                            on_click=lambda e: EliminarReservaCliente(page, db, TextNombre, TextTelefono),
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
                            on_click=lambda e: back_to_first_view(page, db),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )

    eliminar_reserva = ft.Container(
        width=315 * 5,
        content=ft.Column(
            [
                ft.Text("¡Elimina tu reserva!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text("Por favor, introduzca los datos de contacto asociados a su reserva:", size=28, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                TextNombre,
                TextTelefono,
                ft.Row(
                    [
                        BotonEditar,
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
        eliminar_reserva,
        contact_section,
        )