import sqlite3
import flet as ft
from flet import TextField, ElevatedButton, DataTable, DataColumn, DataRow, DataCell, Row, Text, Page

# Variables globales para los campos y el DataTable
titulo = None
autor = None
editorial = None
genero = None
volumen = None
precio = None
stock = None
data_table = None
agregar_btn = None

def init_fields(page):
    global titulo, autor, editorial, genero, volumen, precio, stock, agregar_btn, data_table
    
    titulo = TextField(label="Título")
    autor = TextField(label="Autor")
    editorial = TextField(label="Editorial")
    genero = TextField(label="Género")
    volumen = TextField(label="Volumen", width=80)
    precio = TextField(label="Precio", width=80)
    stock = TextField(label="Stock", width=80)
    
    agregar_btn = ElevatedButton(text="Agregar Manga", on_click=lambda e: agregar_manga(e, page))

    data_table = DataTable(columns=[
        DataColumn(Text("ID")),
        DataColumn(Text("Título")),
        DataColumn(Text("Autor")),
        DataColumn(Text("Editorial")),
        DataColumn(Text("Género")),
        DataColumn(Text("Volumen")),
        DataColumn(Text("Precio")),
        DataColumn(Text("Stock")),
        DataColumn(Text("Acciones")),
    ])

def conectar_bd():
    conn = sqlite3.connect('mangas.db')
    return conn

def listar_mangas(page):
    global data_table
    data_table.rows.clear()
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas")
    rows = cursor.fetchall()

    for row in rows:
        data_table.rows.append(DataRow(cells=[
            DataCell(Text(str(row[0]))),  # ID
            DataCell(Text(row[1])),        # Título
            DataCell(Text(row[2])),        # Autor
            DataCell(Text(row[3])),        # Editorial
            DataCell(Text(row[4])),        # Género
            DataCell(Text(str(row[5]))),   # Volumen
            DataCell(Text(str(row[6]))),   # Precio
            DataCell(Text(str(row[7]))),   # Stock
            DataCell(Row([
                ElevatedButton(text="Editar", on_click=lambda e, id=row[0]: editar_manga(id, page)),
                ElevatedButton(text="Eliminar", on_click=lambda e, id=row[0]: eliminar_manga(id, page))
            ]))
        ]))
    
    conn.close()
    data_table.update()

def agregar_manga(e, page):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mangas (titulo, autor, editorial, genero, volumen, precio, stock)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        titulo.value, autor.value, editorial.value, genero.value,
        int(volumen.value), float(precio.value), int(stock.value)
    ))
    conn.commit()
    conn.close()
    listar_mangas(page)
    limpiar_campos()

def editar_manga(id, page):
    global agregar_btn
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        titulo.value = row[1]
        autor.value = row[2]
        editorial.value = row[3]
        genero.value = row[4]
        volumen.value = str(row[5])
        precio.value = str(row[6])
        stock.value = str(row[7])
        
        agregar_btn.text = "Actualizar Manga"
        agregar_btn.on_click = lambda e: actualizar_manga(id, page)
        agregar_btn.update()

def actualizar_manga(id, page):
    global agregar_btn
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE mangas SET titulo=?, autor=?, editorial=?, genero=?, volumen=?, precio=?, stock=?
        WHERE id=?
    ''', (
        titulo.value, autor.value, editorial.value, genero.value,
        int(volumen.value), float(precio.value), int(stock.value), id
    ))
    conn.commit()
    conn.close()
    listar_mangas(page)
    limpiar_campos()
    agregar_btn.text = "Agregar Manga"
    agregar_btn.on_click = lambda e: agregar_manga(e, page)
    agregar_btn.update()

def eliminar_manga(id, page):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mangas WHERE id=?", (id,))
    conn.commit()
    conn.close()
    listar_mangas(page)

def limpiar_campos():
    global titulo, autor, editorial, genero, volumen, precio, stock
    titulo.value = ""
    autor.value = ""
    editorial.value = ""
    genero.value = ""
    volumen.value = ""
    precio.value = ""
    stock.value = ""
    titulo.focus()
