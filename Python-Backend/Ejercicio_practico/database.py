import sqlite3
from sqlite3 import Error

DATABASE = './Python-Backend/Ejercicio_practico/library.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(e)
    return conn

def init_db():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tittle TEXT NOT NULL,
        author TEXT NOT NULL,
        publish_year INTEGER
    )
    ''')
    
    # Insertar datos de ejemplo
    example_data = [
        ('El Principito', 'Antoine de Saint-Exupéry', 1943),
        ('Cien años de soledad', 'Gabriel García Márquez', 1967),
        ('1984', 'George Orwell', 1949)
    ]
    
    cursor.executemany(
        'INSERT INTO books (tittle, author, publish_year) VALUES (?, ?, ?)',
        example_data
    )
    
    conn.commit()
    conn.close()