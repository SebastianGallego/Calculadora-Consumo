import flet as ft
from flet import Colors


def tarjeta_consumo(nombre, ambiente, consumo_kwh, icono_equipo, eliminar):
    return ft.Container(
        bgcolor=Colors.WHITE,
        padding=10,
        border_radius=10,
        content=ft.Row(
            [
                ft.Icon(icono_equipo, size=30),
                ft.Column(
                    [
                        ft.Text(nombre, weight="bold"),
                        ft.Text(ambiente, italic=True, size=12),
                        ft.Text(
                            f"{consumo_kwh} kWh/mes", size=12, color=Colors.GREEN_700
                        ),
                    ],
                    expand=True,
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color="red",
                    on_click=lambda _: eliminar(nombre),
                ),
            ]
        ),
    )
