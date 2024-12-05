import flet as ft

third_view_content = []

def editar_reserva(page: ft.Page):
    page.title = "Third View"
    page.add(ft.Text("Third View"))

    # Botón de "volver" que nos regresa a la primera vista
    back_button = ft.ElevatedButton("Back", on_click=lambda e: back_to_first_view(page))
    page.add(back_button)

    
    def back_to_first_view(page: ft.Page):
        # Guardar el contenido de la segunda vista
        global third_view_content
        third_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page)