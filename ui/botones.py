import flet as ft

from session import session


def boton_ambiente(volver):
    return ft.ElevatedButton(
        text="Seleccionar Ambiente",
        icon=ft.Icons.ARROW_BACK,
        width=250,
        height=45,
        bgcolor="#37474F",  # gris azulado oscuro
        color="white",  # texto blanco
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
        ),
        on_click=lambda e: e.page.go(f"/{volver}"),
    )


def boton_volver(volver):
    return ft.ElevatedButton(
        text="Volver",
        icon=ft.Icons.ARROW_BACK,
        width=250,
        height=45,
        bgcolor="#546E7A",  # Gris azulado
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
        ),
        on_click=lambda e: e.page.go(f"/{volver}"),
    )


def boton_equipo(volver):
    return ft.ElevatedButton(
        text="Seleccionar Equipo",
        icon=ft.Icons.ARROW_BACK,
        width=250,
        height=45,
        bgcolor="#37474F",  # gris azulado oscuro
        color="white",  # texto blanco
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
        ),
        on_click=lambda e: e.page.go(f"/{volver}"),
    )


def boton_listado():
    return ft.ElevatedButton(
        text="Lista de equipos cargados",
        icon=ft.Icons.TABLE_VIEW,
        width=250,
        height=45,
        bgcolor="green",  # gris azulado oscuro
        color="white",  # texto blanco
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
        ),
        on_click=lambda e: e.page.go(f"/listado"),
    )


def boton_calcular_consumos():
    def calcular_y_ir(e):
        total_kwh = session.consumo_total

        session.kwh_mes = total_kwh
        session.subtotal_pesos = total_kwh * session.tarifa
        session.cargos_fijos = 5000
        session.total_final = (
            session.subtotal_pesos * session.impuestos + session.cargos_fijos
        )

        e.page.go("/resultados")

    return ft.ElevatedButton(
        text="Calcular Consumo Mensual",
        icon=ft.Icons.ATTACH_MONEY,
        width=250,
        height=45,
        bgcolor="green",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
        ),
        on_click=calcular_y_ir,
    )
