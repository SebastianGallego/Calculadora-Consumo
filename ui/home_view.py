import flet as ft
import os
from ui.tarjetas import tarjeta_icono


# from login import TOKEN_FILE
from config import PROVINCIAS


provincias_Dropdown = ft.Dropdown(
    label="Provincia",
    hint_text="Selecciona una provincia",
    width=250,
    bgcolor="#2C2C2C",
    border_radius=10,
    text_style=ft.TextStyle(color="white"),
    color="white",
    options=[ft.Text("Buenos Aires")],
)


def vista_menu():
    return ft.View(
        "/menu",
        bgcolor="#1A1A1A",
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Calculadora de Energía",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                    ft.Text(
                        "Seleccionar", size=22, weight=ft.FontWeight.BOLD, color="white"
                    ),
                    provincias_Dropdown,
                    # Validar en el clic que tengamos provincia
                    tarjeta_icono(
                        "Calculadora de consumo",
                        "iconos/calculadora.svg",
                        "#0066CC",
                        lambda e: validar_provincia(e),
                    ),
                    tarjeta_icono(
                        "Comparar equipos",
                        "iconos/buscar02.svg",
                        "#0099CC",
                        lambda e: print("Comparar"),
                    ),
                    ft.ElevatedButton(
                        "Cerrar sesión",
                        # icon=ft.icons.LOGOUT,
                        bgcolor="red",
                        color="white",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=20)
                        ),
                        on_click=lambda e: logout(e.page),
                    ),
                ],
            )
        ],
    )


def logout(page: ft.Page):
    # if os.path.exists(TOKEN_FILE):
    # os.remove(TOKEN_FILE)
    print("🔒 Sesión cerrada")
    page.go("/")  # Te vuelve a pedir login


def validar_provincia(e):
    """def cerrar_dialogo(ev):
        e.page.dialog.open = False
        e.page.update()

    if provincias_Dropdown.value is None:
        provincias_Dropdown.border_color = "red"
        provincias_Dropdown.helper_text = "Este campo es obligatorio"
        provincias_Dropdown.update()

        e.page.dialog = ft.AlertDialog(
            title=ft.Text("Error"),
            content=ft.Text("Por favor, selecciona una provincia antes de continuar."),
            actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        e.page.dialog.open = True
        e.page.update()
    else:

        print(f"Provincia seleccionada: {provincias_Dropdown.value}")

        # Buscar en la base de datos esa provincia

        e.page.go("/ambiente")"""
    e.page.go("/ambiente")
