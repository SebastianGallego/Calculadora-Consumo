import flet as ft
from ui.tarjetas import tarjeta_icono
from ui.botones import boton_ambiente
from ui.footer import footer_consumo
from listar_equipos import listar_equipos
from session import session


def vista_consumo(ambiente):

    lista_equipos = listar_equipos(ambiente)
    tarjetas = []

    if lista_equipos:
        for equipo in lista_equipos:
            nombre = equipo["nombre"].capitalize()
            icono = "iconos/" + equipo["icono"] + ".svg"
            tarjetas.append(
                ft.Container(
                    content=tarjeta_icono(
                        nombre,
                        icono,
                        "green",
                        lambda e, equipo=equipo: (
                            setattr(session, "equipo_seleccionado", equipo),
                            e.page.go(f"/carga_consumo/{ambiente}"),
                        ),
                    ),
                    col={"xs": 6, "sm": 4, "md": 3},
                )
            )

    else:
        print("No hay datos")

    return ft.View(
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            f"Seleccionar consumos: {ambiente} ",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.ResponsiveRow(controls=tarjetas),
                        boton_ambiente("ambiente"),
                        footer_consumo(),
                    ],
                ),
            )
        ],
    )
