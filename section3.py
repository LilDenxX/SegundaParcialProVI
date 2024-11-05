import flet as ft
from flet import *
from flet import colors, icons

productos = [
    {"nombre": "SteelBallRun Tomo 1", "precio": "90.000Gs",
        "imagen": "recursos/img/jojo1.jpg"},
    {"nombre": "SteelBallRun Tomo 2", "precio": "90.000Gs",
        "imagen": "recursos/img/jojo2.jpg"},
    {"nombre": "SteelBallRun Tomo 4", "precio": "90.000Gs",
        "imagen": "recursos/img/jojo3.jpg"},
    {"nombre": "SteelBallRun Tomo 10", "precio": "90.000Gs",
        "imagen": "recursos/img/jojo10.jpg"},
]

section3 = Container(
    margin=margin.only(top=10, left=10),
    content=Column(
        controls=[
            Text(
                "Series en auge",
                size=30,
                weight="bold",
                style=TextStyle(font_family="custom_font")
            ),
            Row(
                controls=[
                    Container(
                        margin=margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        bgcolor="#444444",
                        ink=True,
                        on_click=lambda e: print("badge test"),
                        border=border.all(2, "#E1E1E1"),
                        content=Text("Todo", size=13, color="white")
                    ),
                    Container(
                        margin=margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        ink=True,
                        on_click=lambda e: print("badge test"),
                        border=border.all(2, "#E1E1E1"),
                        content=Text("1", size=13, color="white")
                    ),
                    Container(
                        margin=margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        ink=True,
                        on_click=lambda e: print("badge test"),
                        border=border.all(2, "#E1E1E1"),
                        content=Text("2", size=13, color="white")
                    )
                ]
            ),
            # Mover la fila de productos fuera de la fila de controles
            ft.Row(
                controls=[
                    ft.Container(
                        margin=10,
                        content=ft.Column(
                            controls=[
                                ft.Image(
                                    src=producto["imagen"], fit=ft.ImageFit.COVER, height=150
                                ),
                                ft.Text(
                                    producto["nombre"], weight="bold"
                                ),
                                ft.Text(producto["precio"]),
                            ]
                        ),
                        width=150  # Ajusta el ancho de cada contenedor de producto
                    )
                    for producto in productos
                ],
                scroll="auto",
                alignment=ft.MainAxisAlignment.CENTER # Permite el desplazamiento horizontal
            )
        ]
    )
)
