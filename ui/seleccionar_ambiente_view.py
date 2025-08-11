import flet as ft
from ui.tarjetas import tarjeta_icono
from ui.botones import boton_volver
from ui.footer import footer_consumo
from session import session


# === Funciones de UI por ruta ===


def vista_ambiente():
    return ft.View(
        "/ambiente",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "Seleccionar el ambiente",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    content=tarjeta_icono(
                                        "Cocina",
                                        "iconos/horno.svg",
                                        "#FFA726",
                                        lambda e: e.page.go("/consumo_cocina"),
                                    ),
                                    col={"xs": 6, "sm": 4, "md": 3},
                                ),
                                ft.Container(
                                    content=tarjeta_icono(
                                        "Baño",
                                        "iconos/bath.svg",
                                        "#29B6F6",
                                        lambda e: e.page.go("/consumo_baño"),
                                    ),
                                    col={"xs": 6, "sm": 4, "md": 3},
                                ),
                                ft.Container(
                                    content=tarjeta_icono(
                                        "Living",
                                        "iconos/sillon.svg",
                                        "#AED581",
                                        lambda e: e.page.go("/consumo_living"),
                                    ),
                                    col={"xs": 6, "sm": 4, "md": 3},
                                ),
                                ft.Container(
                                    content=tarjeta_icono(
                                        "Piezas",
                                        "iconos/cama.svg",
                                        "#FF7043",
                                        lambda e: e.page.go("/consumo_piezas"),
                                    ),
                                    col={"xs": 6, "sm": 4, "md": 3},
                                ),
                                ft.Container(
                                    content=tarjeta_icono(
                                        "Lavadero",
                                        "iconos/lavarropas.svg",
                                        "#1976D2",
                                        lambda e: e.page.go("/consumo_lavadero"),
                                    ),
                                    col={"xs": 6, "sm": 4, "md": 3},
                                ),
                                ft.Container(
                                    content=tarjeta_icono(
                                        "Varios",
                                        "iconos/aa.svg",
                                        "#424242",
                                        lambda e: e.page.go("/consumo_varios"),
                                    ),
                                    col={"xs": 6, "sm": 4, "md": 3},
                                ),
                            ]
                        ),
                        boton_volver("home"),
                        footer_consumo(),
                    ],
                ),
            )
        ],
    )
