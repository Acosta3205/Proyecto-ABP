import flet as ft

id_fila = None

third_view_content = []

def DatosClienteBuscarReservaModificar(page, db, TextNombre, TextTelefono):
        from utils.validators import DatosClienteBuscarReservaModificar
        DatosClienteBuscarReservaModificar(page, db, TextNombre, TextTelefono)

def buscar_reservas(db , TextNombre, TextTelefono):
        from services.querys import buscar_reservas
        buscar_reservas(db, TextNombre, TextTelefono)

def IrAModificarReserva(page, db, TextNombre, TextTelefono, id_reserva):
        from utils.validators import IrAModificarReserva
        IrAModificarReserva(page, db, TextNombre, TextTelefono, id_reserva)

# Generar filas desde las reservas obtenidas
def generar_tabla_reservas(page, tabla, reservas_cliente_lista):
        """Rellena la tabla con las reservas obtenidas."""
        # Limpia las filas actuales
        tabla.rows.clear()

        # Agrega las nuevas filas
        for reserva in reservas_cliente_lista:
            fila = ft.DataRow(
                data=reserva["id"],
                selected=False,
                cells=[
                    ft.DataCell(ft.Text(reserva["id"])),
                    ft.DataCell(ft.Text(reserva["id_mesa"])),
                    ft.DataCell(ft.Text(reserva["fecha"])),
                    ft.DataCell(ft.Text(reserva["hora"])),
                    ft.DataCell(ft.Text(reserva["num_personas"])),
                    ft.DataCell(ft.Text(reserva["notas"])),
                ],
                on_select_changed=lambda e, reserva=reserva: seleccionar_fila(page, e),
            )
            tabla.rows.append(fila)

        # Actualiza la página para reflejar los cambios
        tabla.update()

def seleccionar_fila(page, e):
    """Al hacer clic en una de las filas de la tabla, la fila se marca como seleccionada."""
    global id_fila
    # Obtener la fila seleccionada
    fila = e.control

    # Obtener el ID de la fila
    row_id = fila.data

    # Guardar el ID de la fila en una variable global
    id_fila = row_id
    
    # Invertir el estado de la fila
    fila.selected = not fila.selected

    print("ID de la fila seleccionada:", row_id)

    print("ID: ", id_fila)

    # Mostrar un mensaje indicando la acción realizada
    page.snack_bar = ft.SnackBar(
            ft.Text(f"Reserva {'seleccionada' if fila.selected else 'deseleccionada'}: {row_id}"),
            open=True,
    )
    
    # Actualizar la página para reflejar los cambios
    page.update()
            
# Crear la tabla
TablaReservas = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("Número de reserva")),
        ft.DataColumn(ft.Text("Mesa")),
        ft.DataColumn(ft.Text("Fecha")),
        ft.DataColumn(ft.Text("Hora")),
        ft.DataColumn(ft.Text("Comensales")),
        ft.DataColumn(ft.Text("Nota")),
    ],
    rows=[],  # Generar filas dinámicamente
    bgcolor="white",
    expand=True,
    width=1575,
)

def vaciar_tabla(e):
    TablaReservas.rows.clear()
    TablaReservas.update()

def editar_reserva(page: ft.Page, db):
    page.title = "Sabores Únicos - Modificar reserva"
    page.route = "/ModificarReserva"
    
    def back_to_first_view(page: ft.Page, db):
        # Guardar el contenido de la segunda vista
        global third_view_content
        third_view_content = page.controls[:]

        # Vacia el contenido de la tabla
        TablaReservas.rows.clear()

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page, db)

    def go_to_sixth_view(page: ft.Page, db):
        # Guardar el contenido de la tercera vista
        global third_view_content
        third_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.sixth_view import ModificarReserva
        ModificarReserva(page, db, id_fila)
         
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
    
    TextNombre.on_change = vaciar_tabla

    TextTelefono = ft.TextField(
                    label="Telefono",
                    hint_text="Introduzca su telefono",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )
    
    TextTelefono.on_change = vaciar_tabla

    BotonBuscarReserva = ft.ElevatedButton(
                            "Buscar reserva",
                            on_click=lambda e: DatosClienteBuscarReservaModificar(page, db, TextNombre, TextTelefono),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )
    
    BotonModificarReserva = ft.ElevatedButton(
                            "Modificar reserva",
                            on_click=lambda e: IrAModificarReserva(page, db, TextNombre, TextTelefono, id_fila),
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

    editar_reserva = ft.Container(
        width=315 * 5,
        content=ft.Column(
            [
                ft.Text("¡Modifica tu reserva!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text("Por favor, introduzca los datos de contacto asociados a su reserva:", size=28, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                TextNombre,
                TextTelefono,
                TablaReservas,
                ft.Row(
                    [   
                        BotonBuscarReserva,
                        BotonModificarReserva,
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
        editar_reserva,
        contact_section,
        )