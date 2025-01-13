# --------------------------------
# Importar librerias necesarias
# --------------------------------
import flet as ft

# ---------------------------------------------------
# Importar funciones para las validaciones de los campos
# ---------------------------------------------------

# Funciones para validar los campos del formulario
def DatosClienteBuscarReservaEliminar(page, db, TextNombre, TextTelefono):
    from utils.validators import DatosClienteBuscarReservaEliminar
    DatosClienteBuscarReservaEliminar(page, db, TextNombre, TextTelefono)

# Funciones para eliminar la reserva del cliente
def EliminarReservaClient(page, db, nombre, telefono, id_fila_eliminar):
    from utils.validators import EliminarReservaCliente
    EliminarReservaCliente(page, db, nombre, telefono, id_fila_eliminar)

# --------------------------------
# Variables globales del programa
# --------------------------------

# Variable global que almacenará el ID de la fila seleccionada en la tabla de reservas
id_fila_eliminar = None

# Variable global para almacenar el contenido de las vista
four_view_content = []

# -------------------------------------------------------
# Funciones para manejar la tabla de reservas
# -------------------------------------------------------

# Crear la tabla para mostrar las reservas del cliente
# ---------------------------------------------------------
TablaReservas2 = ft.DataTable(
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
    width=1575,
)

# Generar filas desde las reservas obtenidas
# ----------------------------------------------
def generar_tabla_reservas_eliminar(page, tabla, reservas_cliente_lista):
    """Obtiene una lista que contendrá las consultas asociadas a los datos del cliente insertados en el formulario y rellena la tabla con la información de cada una de ellas.
        
        Args:
            page (flet.Page): La página actual.
            tabla (ft.DataTable): La tabla que se va a rellenar.
            reservas_cliente_lista (list): Una lista que contendrá las reservas asociadas a los datos del cliente insertados en el formulario, obtenidas de la base de datos mediante la consulta buscar_reservas.
        """
    
    # Limpia las filas actuales
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
            on_select_changed=lambda e, reserva=reserva: seleccionar_fila_eliminar(page, e),
        )
        tabla.rows.append(fila)

    # Actualiza la página para reflejar los cambios
    tabla.update()

# Seleccionar una fila de la tabla de reservas
# ----------------------------------------------

def seleccionar_fila_eliminar(page, e):
    """Permite que al hacer clic en una de las filas de la tabla, la fila se marque como seleccionada.
    
    Args:
        page (flet.Page): La página actual.
        e (ft.DataRow): La fila seleccionada.
    """
    # Declarar una variable global para el ID de la fila, haciendo que sea accesible desde el resto del código
    global id_fila_eliminar

    # Obtener la fila seleccionada
    fila = e.control

    # Obtener el ID de la fila
    row_id = fila.data

    # Guardar el ID de la fila en una variable global
    id_fila_eliminar = row_id
    
    # Invertir el estado de la fila
    fila.selected = not fila.selected

    # Mostrar un mensaje indicando la acción realizada
    page.snack_bar = ft.SnackBar(
            ft.Text(f"Reserva {'seleccionada' if fila.selected else 'deseleccionada'}: {row_id}"),
            open=True,
    )
    
    # Actualizar la página para reflejar los cambios
    page.update()

# Vaciar la tabla
# -----------------------

def vaciar_tabla(e):
    """Permite eliminar todos los registros almacenados en la tabla de reservas.
    
    Args:
        e (ft.Event): El evento de edición de los campos de texto.
    """
    TablaReservas2.rows.clear()
    TablaReservas2.update()

# -------------------------------------------------------
# Funcion principal del programa
# -------------------------------------------------------

def eliminar_reserva(page: ft.Page, db):
    """Genera una nueva vista que contendrá un formulario en el que el usuario deberá introducir sus datos de contacto que utilizó para realizar una reserva.
       Luego, podrá realizar una búsqueda de todas las reservas realizadas por el usuario, las cuales podrá seleccionar para modificarlas en otra vista.

    Args:
        page (ft.Page): La página actual.
        db (pymongo.database.Database): La base de datos de MongoDB.
    """
    page.title = "Sabores Únicos - Eliminar reserva"
    page.route = "/EliminarReservaCliente"
    
    # -------------------------------------------------------
    # Funciones para manejar la navegacion entre las vistas
    # -------------------------------------------------------

    def back_to_first_view(page: ft.Page, db):
        """"Función para volver a la vista principal.

        Args:
            page (ft.Page): La página actual.
            db (pymongo.database.Database): La base de datos de MongoDB.
        """
        """Vacía el contenido de la página actual y carga el contenido de la primera vista."""
        # Guardar el contenido de la segunda vista
        global four_view_content
        four_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Vacia el contenido de la tabla
        TablaReservas2.rows.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page, db)

    # -------------------------------------------------------------------------
    # TextEdit para el manejo de datos de los clientes en la base de datos
    # --------------------------------------------------------------------------

    # Campos de texto nombre
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

    # Campos de texto telefono
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
    
    # -------------------------------------------------------------------------
    # Button para el manejo de los datos de reserva y navegacion de vistas
    # --------------------------------------------------------------------------

    # Boton para buscar reserva y mostrar la tabla
    BotonBuscarReserva = ft.ElevatedButton(
                            "Buscar reserva",
                            on_click=lambda e: DatosClienteBuscarReservaEliminar(page, db, TextNombre, TextTelefono),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )
    
    # Boton para eliminar la reserva
    BotonEliminarReservaCliente = ft.ElevatedButton(
                            "Eliminar reserva",
                            on_click=lambda e: EliminarReservaClient(page, db, TextNombre, TextTelefono, id_fila_eliminar),
                            style=ft.ButtonStyle(
                                bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, 
                                color={"": "white" , ft.ControlState.HOVERED: "black"}, 
                                side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, 
                                padding=20, 
                                text_style=ft.TextStyle(size=18)
                            ),
                        )
    
    # Boton para volver a la primera vista
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
                                          on_click=lambda e: back_to_first_view(page), 
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

    # Contenedor para la sección de eliminar reserva
    # ------------------------------------------------
    eliminar_reserva = ft.Container(
        width=315 * 5,
        content=ft.Column(
            [
                ft.Text("Elimina tu reserva!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text("Por favor, introduzca los datos de contacto asociados a su reserva:", size=28, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                TextNombre,
                TextTelefono,
                TablaReservas2,
                ft.Row(
                    [   
                        BotonBuscarReserva,
                        BotonEliminarReservaCliente,
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
        eliminar_reserva,
        contact_section,
        )