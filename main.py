import flet as ft
from flet import Page
import appmenu
import section1  # Importa el módulo section1 correctamente
import section2
import section3
import crud  # Importa el módulo CRUD

def main(page: Page):
    page.fonts = {
        "custom_font": "recursos/fonts/RobotoCondensed-Regular.ttf"
    }

    page.padding = 0
    page.spacing = 0
    page.scroll = "auto"
    page.bgcolor = "#1E1E2C"
    page.window_width = 375
    page.window_height = 667
    page.update()

    crud.init_fields(page)  # Inicializa los campos del CRUD

    page.add(
        appmenu.appmenu,
        section1.section1(page),  # Llama a la función section1 correctamente
        section2.section2,
        section3.section3,
    )

ft.app(target=main)
