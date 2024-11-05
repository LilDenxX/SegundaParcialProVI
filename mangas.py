import sqlite3

# Conectar a la base de datos (creará la base de datos si no existe)
conn = sqlite3.connect('mangas.db')
cursor = conn.cursor()

# Crear la tabla de mangas
cursor.execute('''
CREATE TABLE IF NOT EXISTS mangas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    editorial TEXT,
    genero TEXT,
    volumen INTEGER,
    precio REAL,
    stock INTEGER
)
''')

# Insertar algunos datos de ejemplo
mangas_ejemplo = [
    ("DanDaDan", "Yukinobu Tatsu", "Shueisha", "Acción", 2, 70000.0, 10),
    ("Chainsaw Man", "Tatsuki Fujimoto", "Shueisha", "Acción", 3, 75000.0, 5),
    ("Jujutsu Kaisen", "Gege Akutami", "Shueisha", "Fantasia", 8, 80000.0, 8),
    ("One Piece", "Eiichiro Oda", "Shueisha", "Aventura", 101, 60000.0, 15),
    ("Spy x Family", "Tatsuya Endo", "Shueisha", "Comedia", 6, 65000.0, 7),
]

# Insertar los datos de ejemplo en la tabla
cursor.executemany('''
INSERT INTO mangas (titulo, autor, editorial, genero, volumen, precio, stock)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', mangas_ejemplo)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada y datos de ejemplo insertados.")
