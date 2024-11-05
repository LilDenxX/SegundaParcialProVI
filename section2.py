import flet as ft
from flet import colors, icons

# Datos de ejemplo para el catálogo de productos
productos = [
    {"nombre": "DanDaDan Tomo 2", "precio": "70.000Gs", "imagen": "recursos/img/dan2.jpg"},
    {"nombre": "DanDaDan Tomo 3", "precio": "70.000Gs", "imagen": "recursos/img/dan3.jpg"},
    {"nombre": "DanDaDan Tomo 4", "precio": "70.000Gs", "imagen": "recursos/img/dan4.jpg"},
    {"nombre": "DanDaDan Tomo 5", "precio": "70.000Gs", "imagen": "recursos/img/dan5.jpg"},
]

# Sección 2
section2 = ft.ResponsiveRow(
    [
        ft.Container(
            bgcolor="#1E1E2C",
            border_radius=ft.border_radius.only(top_left=30, top_right=30),
            padding=0,
            margin=ft.margin.symmetric(vertical=30),
            content=ft.Column(
                col={"sm": 12, "md": 12, "lg": 12},
                controls=[
                    # Contenedor para el input de búsqueda
                    ft.Container(
                        bgcolor="#252535",
                        border_radius=30,
                        content=ft.Row(
                            controls=[
                                ft.TextField(
                                    border="none",
                                    prefix_icon=icons.SEARCH,
                                    color="E4E4E7",
                                    label="¿Buscas algo?",
                                ),
                            ]
                        ),
                    ),
                    # Texto "En tendencia" debajo de la barra de búsqueda
                    ft.Text("En tendencia!", size=20, weight="bold", color="white", style=ft.TextStyle(font_family="custom_font")),

                    # Card de ejemplo
                    ft.Card(
                        elevation=30,
                        content=ft.Container(
                            border_radius=30,
                            bgcolor="#fa1511",
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        margin=10,
                                        height=100,
                                        width=75,
                                        content=ft.Image(
                                            src="recursos/img/dan1.jpg",
                                            fit=ft.ImageFit.COVER,
                                        ),
                                    ),
                                    ft.Container(
                                        margin=10,
                                        height=75,
                                        padding=5,
                                        width=120,
                                        border_radius=10,
                                        bgcolor="grey",
                                        content=ft.Column(
                                            controls=[
                                                ft.Text("DanDaDan", weight="bold", size=13),
                                                ft.Text("70.000Gs", weight="bold", size=15),
                                                ft.Text("Pedir", weight="bold", size=14),
                                            ],
                                            alignment="center",
                                            spacing=0,
                                        ),
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Icon(name="attach_money", color="white", size=30),
                                                    ft.Text("Pagar", color="white", size=15, weight="bold"),
                                                ],
                                                alignment="center",
                                                spacing=5,  # Ajustar espacio entre controles
                                            ),
                                            ft.Row(
                                                controls=[
                                                    ft.Icon(name="add_box", color="white", size=30),
                                                    ft.Text("Mas", color="white", size=15, weight="bold"),
                                                ],
                                                alignment="center",
                                                spacing=5,  # Ajustar espacio entre controles
                                            ),
                                        ]
                                    ),
                                ],
                                alignment="space-between",  # Ajustar alineación para mejor diseño
                            ),
                        ),
                    ),
                    # Sección de productos (simulando un carrusel con una fila)
                    ft.Row(
                        controls=[
                            ft.Container(
                                margin=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Image(src=producto["imagen"], fit=ft.ImageFit.COVER, height=150),
                                        ft.Text(producto["nombre"], weight="bold"),
                                        ft.Text(producto["precio"]),
                                    ]
                                ),
                                width=150,  # Ajusta el ancho de cada contenedor de producto
                            )
                            for producto in productos
                        ],
                        scroll="auto",
                        alignment=ft.MainAxisAlignment.CENTER,  # Permite el desplazamiento horizontal
                    ),
                ],
            ),
        )
    ]
)
