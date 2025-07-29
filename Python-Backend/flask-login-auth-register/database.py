import sqlite3
import os
#Nos sirve para encriptar la contraseña y posteriormente desencriptarla
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = "./Python-Backend/flask-login-auth-register/database.db"

#Inicializamos nuestra base de datos
def init_db():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  #Crear la tabla de usuarios
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
  )
  """)
  #Guardamos los cambios
  conn.commit()
  #Cerramos la conexion
  conn.close()
  print(
    f"Base de datos inicializada en {DATABASE} con exito"
  )
  
#Crear un usuario

def create_user(email, username, password):
  try:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    #hashear mi contraseña
    hashed_pw = generate_password_hash(password)
    
    cursor.execute("""
    INSERT INTO users (email, username, password)
    VALUES (?, ?, ?)
    """, (email, username, hashed_pw))
    #Guardamos los cambios
    conn.commit()
    return True
  except sqlite3.IntegrityError as e:
    print(f"Error al crear el usuario: {e}")
    return False
  finally:
    conn.close()
    
def verify_user(email, password):
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  
  cursor.execute("SELECT * FROM users WHERE email = ?", (email))
  user = cursor.fetchone()
  conn.close()
  
  if user and check_password_hash(user[1], password):
    return user[0]
  else:
    return None