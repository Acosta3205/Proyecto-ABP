#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

import flet as ft

#-------------------------------------------------------
# Variables globales del la pagina del programa
#-------------------------------------------------------

# Variable global que almacenará el ID de la fila seleccionada en la tabla de reservas
id_fila = None

# Variable global que almacenará el contenido de la vista actual
third_view_content = []

#-------------------------------------------------------
# Importación de las funciones necesarias
#-------------------------------------------------------

def DatosClienteBuscarReservaModificar(page, db, TextNombre, TextTelefono):
        from utils.validators import DatosClienteBuscarReservaModificar
        DatosClienteBuscarReservaModificar(page, db, TextNombre, TextTelefono)

def IrAModificarReserva(page, db, TextNombre, TextTelefono, id_reserva):
        from utils.validators import IrAModificarReserva
        IrAModificarReserva(page, db, TextNombre, TextTelefono, id_reserva)

# -------------------------------------------------------
# Funciones principales de la vista
# -------------------------------------------------------

# Generar filas desde las reservas obtenidas
def generar_tabla_reservas_modificar(page, tabla, reservas_cliente_lista):
        """Obtinene una lista que contendrá las consultas asociadas a los datos del cliente insertados en el formulario y rellena la tabla con la información de cada una de ellas.
        
        Args:
            page (flet.Page): La página actual.
            tabla (ft.DataTable): La tabla que se va a rellenar.
            reservas_cliente_lista (list): Una lista que contendrá las consultas asociadas a los datos del cliente insertados en el formulario.
        """
        # Limpia las filas actuales de la tabla
        tabla.rows.clear()

        # Añade cada uno de los registros de la lista a la tabla
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
    """Permite que al hacer clic en una de las filas de la tabla, la fila se marque como seleccionada.
    
    Args:
        page (flet.Page): La página actual.
        e (ft.DataRow): La fila seleccionada.
    """
    # Declarar una variable global para el ID de la fila, haciendo que sea accesible desde el resto del código
    global id_fila
    
    # Obtener la fila seleccionada de la tabla
    fila = e.control

    # Obtener el ID de la fila seleccionada
    row_id = fila.data

    # Guardar el ID de la fila en la variable global
    id_fila = row_id
    
    # Invertir el estado de la fila
    fila.selected = not fila.selected

    # Mostrar un mensaje indicando la acción realizada por el usuario
    page.snack_bar = ft.SnackBar(
            ft.Text(f"Reserva {'seleccionada' if fila.selected else 'deseleccionada'}: {row_id}"),
            open=True,
    )
    
    # Actualizar la página para reflejar los cambios
    page.update()
            
# Crear la tabla TablaReservas
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

# Función para vaciar las filas de la tabla
def vaciar_tabla(e):
    """Permite eliminar todos los registros almacenados en la tabla de reservas.

    Args:
        e (ft.Event): El evento de edición de los campos de texto.
    """
    TablaReservas.rows.clear()
    TablaReservas.update()

def editar_reserva(page: ft.Page, db):
    """Genera una nueva vista que contendrá un formulario en el que el usuario deberá introducir sus datos de contacto que utilizó para realizar una reserva.
       Luego, podrá realizar una búsqueda de todas las reservas realizadas por el usuario, las cuales podrá seleccionar para modificarlas en otra vista.

    Args:
        page (ft.Page): La página actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    page.title = "Sabores Únicos - Modificar reserva"
    page.route = "/ModificarReserva"
    
    def back_to_first_view(page: ft.Page, db):
        """"Función para volver a la vista principal.

        Args:
            page (ft.Page): La página actual.
            db (pymongo.database.Database): La base de datos de MongoDB.
        """
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
    
    # Asociar la función de vaciar_tabla a cuando se realiza un cambio en el campo TextNombre
    TextNombre.on_change = vaciar_tabla

    # Campo de texto para el teléfono
    TextTelefono = ft.TextField(
                    label="Telefono",
                    hint_text="Introduzca su telefono",
                    bgcolor="white",
                    border_color="white",
                    label_style=ft.TextStyle(color="black", weight=ft.FontWeight.W_900),
                    border=ft.InputBorder.NONE,
                    filled=True,
                )

    # Asociar la función de vaciar_tabla a cuando se realiza un cambio en el campo TextTelefono    
    TextTelefono.on_change = vaciar_tabla

    #-------------------------------------------------------
    # Botones para el formulario
    #-------------------------------------------------------

    # Botón para buscar reservas en la base de datos
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
    
    # Botón para pasar a la vista de modificar una reserva
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
    
    # Botón para regresar a la vista principal
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

    page.add(
        ImageHeader,
        Header,
        editar_reserva,
        contact_section,
        )