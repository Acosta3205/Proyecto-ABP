import flet as ft

primera_view_content = []

def main(page: ft.Page):
    page.title = "Restaurante Sabores Únicos"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#000000"

    # Alineación de la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Header
    header = ft.Container(
        content=ft.Image(src="images/logo.png", fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
    )

    # Welcome Section
    welcome_section = ft.Container(
        content=ft.Column(
            [
                ft.Text("¡Bienvenidos a nuestra casa!", size=24, weight=ft.FontWeight.W_600, color="#FFC061"),
                ft.Text(
                    "Bienvenidos a Sabores Únicos, un restaurante donde la tradición y la creatividad se fusionan para deleitar tu paladar. Nos especializamos en ofrecer una experiencia gastronómica inolvidable con nuestros exquisitos platos de pasta, tacos llenos de sabor y postres irresistibles."
                    "\nEn Sabores Únicos, creemos que cada comida es una oportunidad para crear momentos especiales. Nuestra carta combina recetas clásicas con toques innovadores, utilizando ingredientes frescos y de la más alta calidad. Desde pastas artesanales preparadas con pasión, hasta tacos con combinaciones únicas y postres que despiertan los sentidos, cada bocado es una celebración de los mejores sabores.",
                    size=20,
                    text_align=ft.TextAlign.JUSTIFY,
                    color="white",
                ),
            ],
            spacing=15,
        ),
        padding=20,
    )                    

    # Images Section
    
    # Carrusel de imágenes de pasta
    images_pasta = ft.Row(width=309 * 5, wrap=False, scroll="auto")
    for i in range(0, 10):
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
    images_postres = ft.Row(width=309 * 5, wrap=False, scroll="auto")
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

    # Contenedor principal alineado al centro
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



    def navegar_realizar_reserva(e):
        # Guardar el contenido de la primera vista
        global primera_view_content
        primera_view_content = page.controls[:]

        # Limpiar la pantalla
        page.controls.clear()

        # Ir a la segunda vista
        page.update()

        # Importar la segunda vista
        from views.second_view import realizar_reserva
        realizar_reserva(page)

    def navegar_editar_reserva(e):
        # Guardar el contenido de la primera vista
        global primera_view_content
        primera_view_content = page.controls[:]

        # Limpiar la pantalla
        page.controls.clear()

        # Ir a la segunda vista
        page.update()

        # Importar la segunda vista
        from views.third_view import editar_reserva
        editar_reserva(page)

    def navegar_eliminar_reserva(e):
        # Guardar el contenido de la primera vista
        global primera_view_content
        primera_view_content = page.controls[:]

        # Limpiar la pantalla
        page.controls.clear()

        # Ir a la segunda vista
        page.update()

        # Importar la segunda vista
        from views.four_view import eliminar_reserva
        eliminar_reserva(page)

    # Contenedor para las columnas de reservas
    reserva_section = ft.Container(
        content=ft.Row(
            [
                # Columna para realizar una reserva
                ft.Column(
                    [
                        ft.ElevatedButton("Realizar Reserva", on_click=navegar_realizar_reserva),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    width=180,
                ),
                # Columna para editar la reserva
                ft.Column(
                    [
                        ft.ElevatedButton("Editar Reserva", on_click=navegar_editar_reserva),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    width=180,
                ),
                # Columna para eliminar la reserva
                ft.Column(
                    [
                        ft.ElevatedButton("Eliminar Reserva", on_click=navegar_eliminar_reserva),
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

    # Contact Section
    contact_section = ft.Container(
        content=ft.Column(
            [
                ft.Text("Contáctanos", size=24, weight=ft.FontWeight.W_600),
                ft.Text("📍 Dirección: Calle Sabores, 123, Ciudad Gourmet"),
                ft.Text("📞 Teléfono: +34 623 456 789"),
                ft.Text("📧 Correo: contacto@saboresunicos.com"),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        padding=20,
        bgcolor=ft.colors.AMBER_50,
        border_radius=10,
    )

    # Layout
    page.add(
        header,
        welcome_section,
        container,
        reserva_section,
        contact_section,
    )
