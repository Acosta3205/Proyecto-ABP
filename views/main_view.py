import flet as ft

primera_view_content = []

def main(page: ft.Page):
    page.title = "Restaurante Sabores Únicos"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT

    # Header
    header = ft.Container(
        content=ft.Text("Restaurante Sabores Únicos", size=30, weight=ft.FontWeight.BOLD),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.INDIGO_400,
        padding=20,
    )

    # Welcome Section
    welcome_section = ft.Container(
        content=ft.Column(
            [
                ft.Text("¡Bienvenidos a nuestra casa!", size=24, weight=ft.FontWeight.W_600),
                ft.Text(
                    "Disfruta de los mejores sabores y experiencias en nuestro restaurante. "
                    "Te ofrecemos una selección única de platillos preparados con amor y los mejores ingredientes.",
                    size=16,
                    text_align=ft.TextAlign.JUSTIFY,
                ),
            ],
            spacing=15,
        ),
        padding=20,
    )

    # Sample Menu Section
    menu_section = ft.Container(
        content=ft.Column(
            [
                ft.Text("Nuestro Menú Destacado", size=24, weight=ft.FontWeight.W_600),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("🌮 Tacos Especiales", weight=ft.FontWeight.W_500),
                                    ft.Text("Deliciosos tacos con una mezcla única de sabores."),
                                ],
                                spacing=5,
                            ),
                            padding=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("🍝 Pasta Artesanal", weight=ft.FontWeight.W_500),
                                    ft.Text("Hecha a mano con nuestras recetas tradicionales."),
                                ],
                                spacing=5,
                            ),
                            padding=10,
                            bgcolor=ft.colors.LIGHT_BLUE_100,
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("🍰 Postres Caseros", weight=ft.FontWeight.W_500),
                                    ft.Text("Endulza tu día con nuestras deliciosas creaciones."),
                                ],
                                spacing=5,
                            ),
                            padding=10,
                            bgcolor=ft.colors.PINK_100,
                            border_radius=10,
                        ),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
        ),
        padding=20,
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
                ft.Text("📞 Teléfono: +34 123 456 789"),
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
        menu_section,
        reserva_section,
        contact_section,
    )
