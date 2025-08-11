import flet as ft
from flet import icons


def main(page: ft.Page):
    page.window_width = 390
    page.window_height = 700
    page.window_resizable = False

    page.add(ft.Icon(icons.ARROW_BACK))


ft.app(target=main, view=ft.FLET_APP)
