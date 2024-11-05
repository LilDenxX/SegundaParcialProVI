import flet as ft
from flet import *

# Importa las variables globales y funciones del CRUD
import crud

def mostrar_crud(e, page):
    page.controls.clear()  # Limpiar los controles actuales
    page.add(
        crud.titulo, crud.autor, crud.editorial, crud.genero, crud.volumen, crud.precio, crud.stock, crud.agregar_btn, crud.data_table
    )
    crud.listar_mangas(page)
    page.update()

def section1(page):
    return Container(
        bgcolor="#2D2D3A",
        padding=20,
        height=60,
        content=Column([
            Row([
                Container(
                    ink=True,
                    on_click=lambda e: mostrar_crud(e, page),  # Llama a mostrar_crud al hacer clic
                    content=Row([
                        Icon(name="newspaper_rounded", color="FF577F", size=20),
                        Text("Catálogo", size=15, color="E4E4E7", style=ft.TextStyle(font_family="custom_font"))
                    ], spacing=1)
                ),
                Container(
                    ink=True,
                    on_click=lambda e: print("Inicio"),
                    content=Row([
                        Icon(name="home", color="FF577F", size=20),
                        Text("Inicio", size=15, color="E4E4E7", style=ft.TextStyle(font_family="custom_font"))
                    ], spacing=1)
                ),
                Container(
                    ink=True,
                    on_click=lambda e: print("Carrito"),
                    content=Row([
                        Icon(name="shopping_cart", color="FF577F", size=20),
                        Text("Carrito", size=15, color="E4E4E7", style=ft.TextStyle(font_family="custom_font"))
                    ], spacing=1)
                ),
            ], spacing=0, alignment="spaceEvenly"
            )
        ], alignment="start")
    )
