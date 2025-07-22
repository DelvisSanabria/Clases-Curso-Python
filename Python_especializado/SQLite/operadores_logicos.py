#Operadores logicos en SQLite 
#Los operadores logicos son utilizados para combinar condiciones en una consulta SQL

import sqlite3

conn = sqlite3.connect("./Python_especializado/SQLite/Agenda/agenda.db")

cursor = conn.cursor()

#1 operador "AND" nos sirve para combinar dos o mas condiciones y devolver resultados que cumplan todas las condiciones

cursor.execute("SELECT * FROM contacts WHERE name = 'Cris' AND phone = '123456789'")
print(cursor.fetchall())  # Devuelve todos los contactos que tienen el nombre "Cris" y el telefono "123456789"

#2 operador "OR" nos sirve para combinar dos o mas condiciones y devolver resultados que cumplan al menos una de las condiciones

cursor.execute("SELECT * FROM contacts WHERE name = 'Cris' OR phone = '123456789'")
print(cursor.fetchall())  # Devuelve todos los contactos que tienen el nombre "Cris"

#3 operador "NOT" nos sirve para negar una condicion y devolver resultados que no cumplan la condicion
cursor.execute("SELECT * FROM contacts WHERE NOT name = 'Cris'")
print(cursor.fetchall())  # Devuelve todos los contactos que no tienen el nombre "Cris"