#Las consultas Avanzadas de SQLite son aquellas que van mas alla de las consultas basicas, como por ejemplo, las consultas que involucran JOIN

#Necesitaremos crear dos tablas 

#1 categories para agrupar los productos por categorias
#2 products para almacenar los productos y todos


#Importamos sqlite3 para trabajar con bases de datos SQLite 
import sqlite3

#creamos nuestra clase DBManager

class DBAdvanceManager:
  
  def __init__(self, db_name="./Python_especializado/SQLite/SQLite_Avanzado/store.db"):
    self.db_name = db_name
    self.conn = None
    self.cursor = None
    
  #Tengo que crear un metodo que le permita a mi clase conectarse a una base de datos
  
  def connect(self):
    try:
      self.conn = sqlite3.connect(self.db_name)
      self.cursor = self.conn.cursor()
      print(f"Conectado a la base de datos {self.db_name}")
    except sqlite3.Error as e:
      print(f"Error al conectar a la base de datos: {e}")
  
  #Necesito un metodo para cerrar mi conexion con la base de datos
  def close(self):
    if self.conn:
      self.conn.close()
      print(f"Desconectado de la base de datos {self.db_name}")
      
  #Necesito un metodo para crear tablas en mi base de datos
  def setup_database(self):
    try:
      #Establezco mi conexion
      self.connect()
      self.cursor.execute("""
                          CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE NOT NULL
                          )
                          """)
      self.conn.commit()
      print(f"Tabla categories creada con exito")
      
      self.cursor.execute("""
                          CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            price REAL NOT NULL,
                            stock INTEGER NOT NULL,
                            category_id INTEGER,
                            FOREIGN KEY (category_id) REFERENCES categories (id)
                          )
                          """)
      self.conn.commit()
      print(f"Tabla products creada con exito")
      
      self.insert_sample_data()
    except sqlite3.Error as e:
      print(f"Error al crear las tablas categories y products: {e}")
    finally:
      self.close()
  
  #Necesito mis metodos CRUD para ingresar datos a mi agenda
  
  #Create
  def insert_sample_data(self):
    try:
      self.connect()
      self.cursor.execute("SELECT COUNT(*) FROM categories;")
      if self.cursor.fetchone()[0] == 0:
        print("Insertando datos de ejemplo en la tabla categories")
        categories = [
          ("Electronics",),
          ("Clothing",),
          ("Home",),
          ("Books",),
          ("Foods",)
        ]
        self.cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)
        self.conn.commit()
        print(f"{len(categories)} categorias insertadas con exito")
      # Insertar datos de ejemplo en la tabla produ
      self.cursor.execute("SELECT COUNT(*) FROM products;")
      if self.cursor.fetchone()[0] == 0:
        print("Insertando datos de ejemplo en la tabla products")
        products = [
          ("Laptop", 1000.0, 10, 1),
          ("Shirt", 20.0, 50, 2),
          ("Table", 500.0, 5, 3),
          ("Book", 10.0, 20, 4),
          ("Bread", 2.0, 100, 5),
          ("Smartphone", 800.0, 15, 1),
          ("Jeans", 30.0, 40, 2),
          ("Chair", 150.0, 8, 3),
          ("Novel", 15.0, 25, 4),
          ("Pizza", 10.0, 60, 5)
        ]
        self.cursor.executemany("INSERT INTO products (name, price, stock, category_id) VALUES (?, ?, ?, ?)", products)
        self.conn.commit()
      else:
        print("La tabla products ya contiene datos, no se insertaron datos de ejemplo")
    except sqlite3.Error as e:
      print(f"Error al insertar datos de ejemplo: {e}")
    finally:
      self.close()
        