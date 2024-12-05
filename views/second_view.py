import flet as ft

second_view_content = []

def realizar_reserva(page: ft.Page):
    page.title = "Second View"
    page.add(ft.Text("Second View"))
    
    # Botón de "volver" que nos regresa a la primera vista
    back_button = ft.ElevatedButton("Back", on_click=lambda e: back_to_first_view(page))
    page.add(back_button)

    def back_to_first_view(page: ft.Page):
        # Guardar el contenido de la segunda vista
        global second_view_content
        second_view_content = page.controls[:]

        # Limpia el contenido de la página actual
        page.controls.clear()

        # Actualiza la página para reflejar los cambios
        page.update()

        from views.main_view import main
        main(page)


