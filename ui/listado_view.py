# Ventana con la lista de equipos cargados
# que con un icono permita borrar el equiupo cargado
# Botones de agregar equipo, cambiar ambiente o "Ver Resultado"
# Cada equipo agregado se muestra una tarjeta con:
#   icono equipo      - Nombre (Ambiente)   -  x kwh/mes   / icono eliminar

import flet as ft
from ui.botones import boton_ambiente, boton_calcular_consumos
from ui.tarjeta_consumo_lista import tarjeta_consumo
from session import session
from flet import Colors


def vista_resultados(page: ft.Page):
    tarjetas_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    texto_total = ft.Text("", size=18, weight=ft.FontWeight.BOLD)

    def eliminar_consumo(index):
        session.consumos.pop(index)
        session.consumo_total = sum(
            (c["watts"] / 1000) * c["horas_dias"] * c["dias_mes"] * c["cantidad"]
            for c in session.consumos
        )
        actualizar_vista()

    def actualizar_vista():
        tarjetas_column.controls.clear()
        for i, consumo in enumerate(session.consumos):
            tarjetas_column.controls.append(
                tarjeta_consumo(consumo, i, eliminar_consumo)
            )

        # Actualizar texto del total
        texto_total.value = f"Consumo total: {session.consumo_total:.2f} kWh/mes"
        page.update()

    actualizar_vista()

    return ft.View(
        route="/resultados",
        controls=[
            ft.Column(
                [
                    ft.Container(
                        padding=20,
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Listado de equipos cargados",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                tarjetas_column,
                                boton_ambiente("ambiente"),
                                boton_calcular_consumos(),
                            ]
                        ),
                    ),
                    ft.Container(
                        bgcolor=Colors.GREEN_600,
                        padding=10,
                        alignment=ft.Alignment(0, 0),
                        content=texto_total,
                    ),
                ],
                expand=True,
            )
        ],
    )
