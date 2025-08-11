"""
ventana con los resultados

Total Kwh / mes (kwh/mes * tarifa) (escalones)
Sub total consumo en Pesos

Cargos Fijos aprox: $

Imp. Municipales, prov, nacionales aprox: $

Total en pesos: $

(observaciones: los resultados son estimativos, algunos municipio
agregan algun costo extra como alumbrado publico)


"""

import flet as ft
from session import session
from ui.botones import boton_volver
from calcular import calcular_consumo


def vista_resultado_total(page):
    # Cálculos

    impuestos = 1  # Si es un multiplicador, puede usarse así
    kwh_mes = session.consumo_total

    cargos_fijos, cargo_variable = calcular_consumo(kwh_mes)
    consumo_pesos = kwh_mes * cargo_variable

    total_pesos = (consumo_pesos * impuestos) + cargos_fijos

    return ft.View(
        route="/resultados",
        controls=[
            ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Text(
                        "Resultados de Consumo", size=24, weight="bold", color="white"
                    ),
                    ft.Divider(),
                    ft.Text(
                        f"Total Kwh/mes: {kwh_mes:.2f} kWh", size=18, color="white"
                    ),
                    ft.Text(
                        f"Subtotal (Consumo): ${consumo_pesos:.2f}",
                        size=18,
                        color="white",
                    ),
                    ft.Text(
                        f"Cargos Fijos Aproximados: ${cargos_fijos:.2f}",
                        size=18,
                        color="white",
                    ),
                    ft.Text(
                        f"Total con Impuestos: ${consumo_pesos * impuestos:.2f}",
                        size=18,
                        color="white",
                    ),
                    ft.Text(
                        f"Total a pagar: ${total_pesos:.2f}",
                        size=20,
                        weight="bold",
                        color="#00E676",
                    ),
                    ft.Divider(),
                    ft.Text("Observaciones:", size=16, weight="bold", color="white"),
                    ft.Text(
                        "Los resultados son estimativos. Algunos municipios pueden agregar costos extras como alumbrado público.",
                        size=14,
                        color="white",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    boton_volver("home"),
                ],
            )
        ],
    )
