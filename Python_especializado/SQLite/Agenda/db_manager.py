#Importamos sqlite3 para trabajar con bases de datos SQLite 
import sqlite3

#creamos nuestra clase DBManager

class DBManager:
  
  def __init__(self, db_name="./Python_especializado/SQLite/Agenda/agenda.db"):
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
  def create_table(self):
    try:
      self.connect()
      self.cursor.execute("""
                          CREATE TABLE IF NOT EXISTS contacts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            phone TEXT UNIQUE NOT NULL,
                            email TEXT NOT NULL,
                          )
                          """)
      self.conn.commit()
      print(f"Tabla contacts creada con exito")
    except sqlite3.Error as e:
      print(f"Error al crear la tabla contacts: {e}")
    finally:
      self.close()
  
  #Necesito mis metodos CRUD para ingresar datos a mi agenda
  
  #Create
  def insert_contact(self,name,phone,email):
    try:
      self.connect()
      self.cursor.execute("INSERT INTO contacts (name,phone,email) VALUES (?,?,?)",(name,phone,email))
      self.conn.commit()
      print(f"Contacto {name} creado con exito")
      return True
    
    except sqlite3.IntegrityError as e:
      print(f"El contacto {name} ya existe en la agenda, porque su numero ya esta registrado")
      return False
    except sqlite3.Error as e:
      print(f"Error al insertar el contacto: {e}")
      return False
    finally:
      self.close()
      
  def insert_many_contacts(self,list_contacts):
    try:
      self.connect()
      self.cursor.executemany("INSERT INTO contacts (name,phone,email) VALUES (?,?,?)",list_contacts)
      self.conn.commit()
      print(f"{len(list_contacts)} contactos creados con exito")
      return True
    except sqlite3.IntegrityError as e:
      print(f"Uno o mas numeros de telefon  ya existen. Por favor verifique")
      return False
    except sqlite3.Error as e:
      print(f"Error al insertar los contactos: {e}")
      return False
    finally:
      self.close()
          
  #Read

  def read_contacts(self):
    try:
      self.connect()
      self.cursor.execute("SELECT * FROM contacts")
      contacts = self.cursor.fetchall()   
      return contacts
    except sqlite3.Error as e:
      print(f"Error al leer los contactos: {e}")
      return []
    finally:
      self.close()
      
  def search_contact(self, columm, value):
    try:
      self.connect()
      if columm not in ["name","phone","email"]:
        print(f"La columna {columm} no existe")
        return []
      #No hay errores y la columna existe
      self.cursor.execute(f"SELECT * FROM contacts WHERE {columm} LIKE ?",(f"%{value}%",))
      contact = self.cursor.fetchall()
      return contact
    except sqlite3.Error as e:
      print(f"Error al buscar el valor: {value} en la columna {columm}: {e}")
      return []
    finally:
      self.close()
      
  #Update
  def update_contact(self,id,new_name=None,new_phone=None,new_email=None):
    try:
      self.connect()
      query_part = []
      values = []
      
      if new_name is not None:
        query_part.append("name = ?")
        values.append(new_name)
      if new_phone is not None:
        query_part.append("phone = ?")
        values.append(new_phone)
      if new_email is not None:
        query_part.append("email = ?")
        values.append(new_email)
      if not query_part:
        print("No se proporcionaron valores para actualizar")
        return False
      
      values.append(id)
      query = ", ".join(query_part)
      self.cursor.execute(f"UPDATE contacts SET {query} WHERE id = ?",(tuple(values)))
      self.conn.commit()
      
      if self.cursor.rowcount > 0:
        print(f"Contacto {id} actualizado con exito")
        return True
      else:
        print(f"Contacto {id} no encontrado")
        return False
    except sqlite3.IntegrityError as e:
      print(f"El contacto {id} ya existe en la agenda, porque su numero ya esta registrado")
      return False
    except sqlite3.Error as e:
      print(f"Error al actualizar el contacto: {e}")
      return False
    finally:
      self.close()
      
  #Delete
  def delete_contact(self, contact_id):
    try:
      self.connect()
      self.cursor.execute("DELETE FROM contacts WHERE id = ?",(contact_id,))
      self.conn.commit()
      if self.cursor.rowcount > 0:
        print(f"Contacto {contact_id} eliminado con exito")
        return True
      else:
        print(f"Contacto {contact_id} no encontrado")
        return False
    except sqlite3.Error as e:
      print(f"Error al eliminar el contacto: {e}")
      return False
    finally:
      self.close()
      
      
#Pruebas

if __name__ == "__main__":
  manager = DBManager()
  manager.connect()
  manager.create_table() #Ejecutenlo 1 sola vez
  
  #Insert
  manager.insert_contact("Herasi","12312133445678","Herasi777@gmail")
  manager.insert_contact("Cris","135652345678","crissivira9@gmail")
  manager.insert_many_contacts([("Herasi","1234768585678","Herasi777@gmail"),("Cris","12343645755678","crissivira9@gmail"),("Delvis","127898089345678","delvissivira9@gmail")])
  
  #Read
  print(manager.read_contacts())
  print(manager.search_contact("name","Cris"))
  
  #Update
  manager.update_contact(1,new_name="PaulaTheRevolution",new_email="paulaDev25@gmail")
  
  #Delete
  manager.delete_contact(3)
  manager.close()