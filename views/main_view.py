#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar la libreria flet
import flet as ft

# Variable global para almacenar el contenido de las vista
primera_view_content = []

#-------------------------------------------------------
# Funcion principal del programa
#-------------------------------------------------------

def main(page: ft.Page, db):
    page.title = "Restaurante Sabores Únicos"
    page.route = "/Home"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#000000"

    # Alineación de la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Fuente de texto
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Roboto": "http://themes.googleusercontent.com/static/fonts/robotoslab/v2/y7lebkjgREBJK96VQi37Zp0EAVxt0G0biEntp43Qt6E.ttf"
    }

    #-------------------------------------------------------
    # Funciones para manejar la navegacion entre las vistas
    #-------------------------------------------------------
    def navegar_realizar_reserva(e):
        """Vacía el contenido de la página actual y carga el contenido de la segunda vista."""
        # Guardar el contenido de la primera vista
        global primera_view_content
        primera_view_content = page.controls[:]

        # Limpiar la pantalla
        page.controls.clear()

        # Ir a la segunda vista
        page.update()

        # Importar la segunda vista
        from views.second_view import realizar_reserva
        realizar_reserva(page, db)

    def navegar_editar_reserva(e):
        """Vacía el contenido de la página actual y carga el contenido de la tercera vista."""
        # Guardar el contenido de la primera vista
        global primera_view_content
        primera_view_content = page.controls[:]

        # Limpiar la pantalla
        page.controls.clear()

        # Ir a la segunda vista
        page.update()

        # Importar la segunda vista
        from views.third_view import editar_reserva
        editar_reserva(page, db)

    def navegar_eliminar_reserva(e):
        """Vacía el contenido de la página actual y carga el contenido de la cuarta vista."""
        # Guardar el contenido de la primera vista
        global primera_view_content
        primera_view_content = page.controls[:]

        # Limpiar la pantalla
        page.controls.clear()

        # Ir a la segunda vista
        page.update()

        # Importar la segunda vista
        from views.four_view import eliminar_reserva
        eliminar_reserva(page, db)

    #-------------------------------------------------------
    # Variables globales del la pagina del programa
    #-------------------------------------------------------

    # Cabecera
    #-------------
    header = ft.Container(
        content=ft.Image(src="images/logo.png", fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
        width=1920,
    )

    # Bienvenida de la pagina y informacion sobre el restaurante
    #-----------------------------------------------------------------
    welcome_section = ft.Container(width=315 * 5,
        content=ft.Column(
            [
                ft.Text("¡Bienvenidos a nuestra casa!", size=38, weight=ft.FontWeight.W_600, color="#FFC061", font_family="Kanit"),
                ft.Text(
                    "Bienvenidos a Sabores Únicos, un restaurante donde la tradición y la creatividad se fusionan para deleitar tu paladar. Nos especializamos en ofrecer una experiencia gastronómica inolvidable con nuestros exquisitos platos de pasta, tacos llenos de sabor y postres irresistibles."
                    "\n\nEn Sabores Únicos, creemos que cada comida es una oportunidad para crear momentos especiales. Nuestra carta combina recetas clásicas con toques innovadores, utilizando ingredientes frescos y de la más alta calidad. Desde pastas artesanales preparadas con pasión, hasta tacos con combinaciones únicas y postres que despiertan los sentidos, cada bocado es una celebración de los mejores sabores."
                    "\n\nNuestro equipo de chefs y personal está comprometido con brindar un servicio cálido y atento, haciendo que cada visita sea una experiencia memorable. Ya sea que vengas a disfrutar de una cena en pareja, una reunión familiar o una comida casual con amigos, en Sabores Únicos te haremos sentir como en casa."
                    "\n\nTe invitamos a descubrir un mundo de sabores que te sorprenderán y a compartir momentos inolvidables con nosotros. ¡Bienvenidos a Sabores Únicos, donde cada plato cuenta una historia llena de pasión y sabor!",
                    size=24,
                    text_align=ft.TextAlign.JUSTIFY,
                    color="white",
                    font_family="Roboto",
                ),
            ],
            spacing=15,
        ),
        padding=20,
    )                    

    # Carrusel de imágenes
    # ----------------------
    # Carrusel de imágenes de pasta
    # ----------------------------------
    images_pasta = ft.Row(width=309 * 5, wrap=False, scroll="auto")
    for i in range(0, 9):
        images_pasta.controls.append(
            ft.Image(
                src=f"images/pasta/{i}.jpg",
                width=300,
                height=300,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    # Carrusel de imágenes de tacos
    # ----------------------------------
    images_tacos = ft.Row(width=309 * 5, wrap=False, scroll="auto")
    for i in range(1, 10):
        images_tacos.controls.append(
            ft.Image(
                src=f"images/tacos/taco-{i}.jpg",
                width=300,
                height=300,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    # Carrusel de imágenes de postres
    # ----------------------------------
    images_postres = ft.Row(width=309 * 5, wrap=False, scroll="auto", on_scroll_interval=100)
    for i in range(0, 9):
        images_postres.controls.append(
            ft.Image(
                src=f"images/postres/{i}.jpg",
                width=300,
                height=300,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    # Contenedor principal donde van los carruseles
    # ------------------------------------------------
    container = ft.Column(
        [
            # Contenedores para los tacos
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("🌮 Tacos Especiales", weight=ft.FontWeight.W_900, size=20),
                        images_tacos,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
                bgcolor= "#FFC061",
                border_radius=10,
            ),

            # Contenedores para las pastas
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("🍝 Pasta Artesanal", weight=ft.FontWeight.W_900, size=20),
                        images_pasta,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
                bgcolor= "#FFC061",
                border_radius=10,
            ),

            # Contenedores para los postres
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("🍰 Postres Caseros", weight=ft.FontWeight.W_900, size=20),
                    images_postres,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
                bgcolor= "#FFC061",
                border_radius=10,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    # Contenedor donde van las opciones de reserva
    #-------------------------------------------------------
   
    reserva_section = ft.Container(
        content=ft.Row(
            [
                # Columna para realizar una reserva
                ft.Column(
                    [
                        ft.ElevatedButton("Realizar Reserva", 
                                          on_click=navegar_realizar_reserva, 
                                          style=ft.ButtonStyle(bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, color={"": "white" , ft.ControlState.HOVERED: "black"}, side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, padding=20, text_style=ft.TextStyle(size=18)))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    width=180,
                ),
                # Columna para editar la reserva
                ft.Column(
                    [
                        ft.ElevatedButton("Editar Reserva", on_click=navegar_editar_reserva, style=ft.ButtonStyle(bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, color={"": "white", ft.ControlState.HOVERED: "black"}, side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, padding=20, text_style=ft.TextStyle(size=18))),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    width=180,
                ),
                # Columna para eliminar la reserva
                ft.Column(
                    [
                        ft.ElevatedButton("Eliminar Reserva", on_click=navegar_eliminar_reserva, style=ft.ButtonStyle(bgcolor={"": "#000000", ft.ControlState.HOVERED: "#FFC061"}, color={"": "white", ft.ControlState.HOVERED: "black"}, side={"": ft.BorderSide(width=3, color="#FFC061"), ft.ControlState.HOVERED: ft.BorderSide(width=3, color="white")}, padding=20, text_style=ft.TextStyle(size=18))),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    width=180,
                ),
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=20,
        alignment=ft.alignment.center,
    )

    # Contenedor para la sección de contacto
    #-------------------------------------------------------
    
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
        header,
        welcome_section,
        container,
        reserva_section,
        contact_section,
    )