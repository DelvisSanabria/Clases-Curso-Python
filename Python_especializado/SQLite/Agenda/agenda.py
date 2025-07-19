from db_manager import DBManager

#Hago mi funcion para mostrar todas las opciones de mi agenda

def show_menu():
  print("\n Gestion de agenda")
  print("1. Crear tabla de contactos (si no existe)")
  print("2. Insertar un contacto")
  print("3. Insertar varios contactos")
  print("4. Mostrar todos los contactos")
  print("5. Buscar un contacto")
  print("6. Actualizar un contacto")
  print("7. Eliminar un contacto")
  print("0. Salir")
  print("-"*50)
  
  
#Creamos nuestra logica para el manejo de la agenda

def run_app():
  #Creamos una instancia de nuestra clase DBManager
  db = DBManager("./Python_especializado/SQLite/Agenda/agenda.db")
  
  while True:
    #Llamamos a la funcion que contiene nuestras opciones
    show_menu()
    option = input("Seleccione una opcion: ")
    
    if option == '1':
      db.create_table()
    elif option =='2':
      name = input("Ingrese el nombre del contacto: ")
      phone = input("Ingrese el telefono del contacto: ")
      email = input("Ingrese el correo del contacto: ")
      db.insert_contact(name,phone,email if email else None)
    elif option == '3':
     insert_contacts = []
     print("Introduce contactos (deja el nombre en blanco para salir)")
     #Pedimos todos los contactos en un bucle infinito
     while True:
       #Tarea: asegurarse de manejar los errores
       name = input("Ingrese el nombre del contacto: ")
       if not name:
         break
       phone = input("Ingrese el telefono del contacto: ")
       email = input("Ingrese el correo del contacto: ")
       insert_contacts.append((name,phone,email if email else None))
     if insert_contacts:
      db.insert_many_contacts(insert_contacts)
     else:
      print("No se proporcionaron contactos para insertar")
    elif option == '4':
      contacts = db.read_contacts()
      if contacts:
        for contact in contacts:
          #Cada contacto se ve asi: (id,nombre,telefono,correo)
          print(f"ID: {contact[0]}, Nombre: {contact[1]}, Telefono: {contact[2]}, Correo: {contact[3] if contact[3] else 'No tiene un correo'}")
    elif option == '5':
      #Tarea: asegurarse de manejar los errores
      search_columm = input("Ingrese la columna (name,phone,email) a buscar: ")
      search_value = input("Ingrese el valor a buscar: ")
      contacts = db.search_contact(search_columm,search_value)
      if contacts:
        print(f"Se encontraron {len(contacts)} contactos con el valor {search_value} en la columna {search_columm}:")
        for contact in contacts:
          #Cada contacto se ve asi: (id,nombre,telefono,correo)
          print(f"ID: {contact[0]}, Nombre: {contact[1]}, Telefono: {contact[2]}, Correo: {contact[3] if contact[3] else 'No tiene un correo'}")
      else:
        print(f"No se encontraron contactos con el valor {search_value} en la columna {search_columm}")
    elif option == '6':
      contacts = input("Ingrese el ID del contacto a actualizar(debe ser un numero): ")
      try:
        #Tarea: asegurarse de manejar los errores
        contact_id = int(contacts)
        new_name = input("Ingrese el nuevo nombre del contacto (dejar en blanco para no actualizar): ")
        new_phone = input("Ingrese el nuevo telefono del contacto (dejar en blanco para no actualizar): ")
        new_email = input("Ingrese el nuevo correo del contacto (dejar en blanco para no actualizar): ")
        
        db.update_contact(contact_id,new_name if new_name else None,new_phone if new_phone else None,new_email if new_email else None)
      except ValueError:
        print("El ID debe ser un numero entero")
    elif option == '7':
      contact_id = input("Ingrese el ID del contacto a eliminar(debe ser un numero): ")
      try:
        #Tarea: asegurarse de manejar los errores
        contact_id = int(contact_id)
        db.delete_contact(contact_id)
      except ValueError:
        print("El ID debe ser un numero entero")
    elif option == '0':
      print("Saliendo...")
      break
    else:
      print("Opcion no valida")


#Cuando este archivo se ejecute, se ejecutara la funcion run_app
if __name__ == "__main__":
  run_app()