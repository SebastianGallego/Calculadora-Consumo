import flet as ft


def main(page: ft.Page):
    page.title = "Prueba Tamaño Fijo"
    page.window_width = 390
    page.window_height = 700
    page.window_resizable = False

    page.add(ft.Text("Ventana fija de app móvil"))


ft.app(target=main, view=ft.FLET_APP)
