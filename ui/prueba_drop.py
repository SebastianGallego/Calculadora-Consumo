import flet as ft


def main(page: ft.Page):
    dropdown = ft.Dropdown(
        label="Selecciona provincia",
        hint_text="Ej: Buenos Aires",
        options=["Buenos Aires", "Córdoba", "Mendoza"],  # SOLO STRINGS
    )

    def mostrar_valor(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Provincia: {dropdown.value}"))
        page.snack_bar.open = True
        page.update()

    page.add(dropdown, ft.ElevatedButton("Aceptar", on_click=mostrar_valor))


ft.app(target=main)
