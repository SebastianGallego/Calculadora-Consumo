import flet as ft


def tarjeta_consumo(consumo: dict, index: int, eliminar_callback):
    kwh_mes = (
        (consumo["watts"] / 1000)
        * consumo["horas_dias"]
        * consumo["dias_mes"]
        * consumo["cantidad"]
    )

    return ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=10,
        border_radius=10,
        margin=ft.Margin(0, 5, 0, 5),
        content=ft.Row(
            [
                ft.Image(
                    src=consumo.get(
                        "icono",
                    ),
                    width=40,
                    height=40,
                    color=ft.colors.BLUE_900,
                ),
                ft.Column(
                    [
                        ft.Text(
                            f'{consumo["equipo"]} ({consumo.get("ambiente", "Sin ambiente")})',
                            weight="bold",
                            color=ft.colors.BLUE_900,
                        ),
                        ft.Text(
                            f'{consumo["cantidad"]}x - {kwh_mes:.2f} kWh/mes',
                            size=12,
                            color=ft.colors.GREEN_700,
                        ),
                    ],
                    expand=True,
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color="red",
                    tooltip="Eliminar equipo",
                    on_click=lambda _: eliminar_callback(index),
                ),
            ]
        ),
    )
