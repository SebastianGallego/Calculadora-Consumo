import time
import flet as ft
from ui.botones import boton_equipo, boton_listado
from ui.tarjetas import tarjeta_icono

from ui.footer import footer_consumo
from session import session  # Asegurate de que tenga equipo_seleccionado


def vista_carga_consumo(ambiente):
    equipo = session.equipo_seleccionado
    nombre_equipo = equipo["nombre"]
    icono = f"iconos/{equipo['icono']}.svg"

    tarjeta_equipo = ft.Container(
        content=tarjeta_icono(nombre_equipo, icono, "green", ""),
        col={"xs": 6, "sm": 4, "md": 3},
    )

    # Inputs
    numero_equipos = ft.TextField(value="1", keyboard_type="number")
    potencia_watts = ft.TextField(value="1500", keyboard_type="number")
    horas_dia = ft.TextField(value="1", keyboard_type="number")
    dias_mes = ft.TextField(value="30", keyboard_type="number")

    # Función para filas alineadas
    def fila_input(titulo, control):
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD),
                    alignment=ft.Alignment(-1, 0),
                    expand=True,
                ),
                ft.Container(content=control, width=80, alignment=ft.Alignment(1, 0)),
            ]
        )

    def calcular_click(e):
        try:

            # Validar que todos los campos estén completos y sean positivos
            campos = {
                "Cantidad": numero_equipos.value,
                "Potencia (W)": potencia_watts.value,
                "Horas por día": horas_dia.value,
                "Días al mes": dias_mes.value,
            }

            for campo, valor in campos.items():
                if not valor.strip():
                    raise ValueError(f"El campo '{campo}' no puede estar vacío.")
                if float(valor) <= 0:
                    raise ValueError(f"El campo '{campo}' debe ser mayor que cero.")

            # Convertir valores
            n_equipo = int(numero_equipos.value)
            potencia = float(potencia_watts.value)
            horas = float(horas_dia.value)
            dias = int(dias_mes.value)

            # Calcular consumo
            consumo = (potencia / 1000) * n_equipo * horas * dias

            # Agregar a la sesión
            session.agregar_consumo(
                nombre_equipo, n_equipo, potencia, horas, dias, ambiente, icono
            )

            # Mostrar resultado
            snackbar = ft.SnackBar(
                content=ft.Text(
                    f"Consumo agregado: {consumo:.1f} kWh/mes\nAcumulado: {session.consumo_total:.1f} kWh/mes"
                ),
                bgcolor="green",
                behavior=ft.SnackBarBehavior.FLOATING,
                duration=2500,
                show_close_icon=True,
            )
            e.page.overlay.append(snackbar)
            snackbar.open = True
            e.page.update()

        except ValueError as ex:
            e.page.overlay.append(
                ft.SnackBar(
                    content=ft.Text(str(ex)),
                    bgcolor="red",
                    behavior=ft.SnackBarBehavior.FLOATING,
                    duration=3000,
                    show_close_icon=True,
                )
            )
            e.page.overlay[-1].open = True
            e.page.update()

        except Exception as ex:
            e.page.dialog = ft.AlertDialog(
                title=ft.Text("Error inesperado"), content=ft.Text(str(ex))
            )
            e.page.dialog.open = True
            e.page.update()

    def limpiar_click(e):
        numero_equipos.value = ""
        potencia_watts.value = ""
        horas_dia.value = ""
        dias_mes.value = ""
        e.page.update()

    return ft.View(
        route="/carga_consumo",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        tarjeta_equipo,
                        fila_input(f"Cantidad de {nombre_equipo}:", numero_equipos),
                        fila_input("Potencia en Watts:", potencia_watts),
                        fila_input("Tiempo de uso por día (horas):", horas_dia),
                        fila_input("Días de uso por mes:", dias_mes),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    text="Calcular",
                                    icon=ft.Icons.CALCULATE,
                                    width=150,
                                    height=45,
                                    bgcolor="green",
                                    color="white",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=6),
                                        padding=20,
                                    ),
                                    on_click=calcular_click,
                                ),
                                ft.ElevatedButton(
                                    text="Limpiar",
                                    icon=ft.Icons.CLEAR,
                                    width=150,
                                    height=45,
                                    bgcolor="red",
                                    color="white",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=6),
                                        padding=20,
                                    ),
                                    on_click=limpiar_click,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        boton_equipo(f"consumo_{ambiente}"),
                        boton_listado(),
                    ],
                ),
            ),
            footer_consumo(),
        ],
    )
