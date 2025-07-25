import sqlite3
import os

# Definimos la ruta de la base de datos
DATABASE_NAME = './Python_Backend/flaks-sqlite/agenda.db'

#crear un metodo para obtener la conexion a la base de datos
def get_db_connection():
    """Establece una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn
  
def initialize_db():
    """Inicializa la base de datos creando las tablas necesarias."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()