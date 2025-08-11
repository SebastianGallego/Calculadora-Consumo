import flet as ft


def tarjeta_icono(texto: str, icono_src: str, color_fondo: str, on_click_fn):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=icono_src, width=50, height=50),
                    ft.Text(
                        texto,
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.Alignment(0, 0),
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            width=140,
            height=140,
            bgcolor=color_fondo,
            border_radius=15,
            alignment=ft.Alignment(0, 0),
            on_click=on_click_fn,
        ),
        elevation=5,
    )
