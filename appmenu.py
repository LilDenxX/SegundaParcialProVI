import flet as ft
from flet import *
from flet import colors, icons

# Creación de la APPBAR 
appmenu = ft.ResponsiveRow(
    [
        ft.Column(
            col={"sm": 12, "md": 12, "lg": 12},
            controls=[
                ft.Container(
                    padding=10,
                    bgcolor="#151521",
                    content=ft.Row(
                        [
                            # Aquí irá el logo de la aplicación
                            ft.Image(src="recursos/img/img.png", fit="contain", width=150, height=75),
                            
                            ft.CircleAvatar(
                                foreground_image_url=("https://png.pngitem.com/pimgs/s/146-1468281_profile-icon-png-transparent-profile-picture-icon-png.png")  # Ruta a tu imagen de avatar
                            ),
                        ],
                        alignment="spaceBetween",
                        spacing=10
                    )
                )
            ]
        )
    ]
)
