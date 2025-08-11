import flet as ft
from ui.seleccionar_ambiente_view import vista_ambiente
from ui.home_view import vista_menu
from ui.consumo_view import vista_consumo
from ui.cargar_consumo_view import vista_carga_consumo
from ui.resultados import vista_resultado_total
from ui.listado_view import vista_resultados
from login import login_google_automatico
from session import session
import os


def envolver_contenido(controles, ruta="/"):
    return ft.View(
        route=ruta,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=390,
                        bgcolor="#1A1A1A",
                        padding=10,
                        content=ft.Column(
                            controls=controles, expand=True, scroll=ft.ScrollMode.AUTO
                        ),
                    )
                ],
            )
        ],
        scroll=ft.ScrollMode.AUTO,
    )


def main(page: ft.Page):
    page.title = "Calculadora de Energía"
    page.scroll = "auto"
    page.bgcolor = "#000000"  # fondo global oscuro fuera del container
    page.window_width = 375
    page.window_height = 812
    page.window_resizable = False

    # --- Login automático con Google ---
    # user_info = login_google_automatico()
    user_info = "Juan Perez"
    session.usuario = user_info  # Guardamos el usuario globalmente

    def on_route_change(e):
        page.views.clear()

        if page.route == "/home":
            page.views.append(envolver_contenido(vista_menu().controls, "/home"))
        elif page.route == "/ambiente":
            page.views.append(
                envolver_contenido(vista_ambiente().controls, "/ambiente")
            )
        elif page.route == "/consumo_living":
            page.views.append(
                envolver_contenido(vista_consumo("living").controls, "/consumo_living")
            )
        elif page.route == "/consumo_baño":
            page.views.append(
                envolver_contenido(vista_consumo("baño").controls, "/consumo_baño")
            )
        elif page.route == "/consumo_cocina":
            page.views.append(
                envolver_contenido(vista_consumo("cocina").controls, "/consumo_cocina")
            )
        elif page.route == "/consumo_piezas":
            page.views.append(
                envolver_contenido(vista_consumo("piezas").controls, "/consumo_piezas")
            )
        elif page.route == "/consumo_lavadero":
            page.views.append(
                envolver_contenido(
                    vista_consumo("lavadero").controls, "/consumo_lavadero"
                )
            )
        elif page.route == "/consumo_varios":
            page.views.append(
                envolver_contenido(vista_consumo("varios").controls, "/consumo_varios")
            )
        elif page.route.startswith("/carga_consumo/"):
            ambiente = page.route.split("/")[2]
            page.views.append(
                envolver_contenido(
                    vista_carga_consumo(ambiente).controls, "/carga_consumo/" + ambiente
                )
            )
        elif page.route == "/listado":
            page.views.append(
                envolver_contenido(vista_resultados(page).controls, "/listado")
            )

        elif page.route == "/resultados":
            page.views.append(
                envolver_contenido(vista_resultado_total(page).controls, "/resultados")
            )
        else:
            page.views.append(
                envolver_contenido([ft.Text("Error de ruta o no autenticado")])
            )

        page.update()

    page.on_route_change = on_route_change
    page.update()

    usuario = "Test"
    page.go("/home" if usuario else "/")


if __name__ == "__main__":
    # Render/Fly/Railway exponen el puerto en la var PORT
    port = int(os.getenv("PORT", "8000"))
    # AppView puede variar según versión de flet
    view = getattr(ft.AppView, "WEB_BROWSER", ft.WEB_BROWSER)
    ft.app(target=main, view=view, host="0.0.0.0", port=port)

# Prueba de web app
