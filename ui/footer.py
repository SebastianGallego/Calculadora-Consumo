import flet as ft
from session import session


def footer_consumo():
    if session.consumo_total == 0:
        return ft.Container(
            expand=False,
            alignment=ft.Alignment(0, 0),
            content=ft.Text(
                "",
                size=28,
                weight=ft.FontWeight.BOLD,
                color="white",
            ),
        )
    else:
        email = session.usuario["email"] if session.usuario else "Invitado"
        return ft.Container(
            expand=False,
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        f"Total: {session.consumo_total:.1f} kWh/mes",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                    ft.Text(
                        f"Sesión: {email}",
                        size=14,
                        italic=True,
                        color="white70",
                    ),
                ],
            ),
        )
