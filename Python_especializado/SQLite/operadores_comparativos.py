#Operadores comparativos en SQLite
#Los operadores comparativos son utilizados para comparar valores en una consulta SQL

import sqlite3

conn = sqlite3.connect("./Python_especializado/SQLite/Agenda/agenda.db")

cursor = conn.cursor()


#1 comparador es el igual (=) nos sirve para comparar si dos valores son iguales
#cursor.execute("SELECT * FROM contacts WHERE name = 'Cris'")
#print(cursor.fetchall()) #Devuelve todos los contactos que tienen el nombre "Cris"

#Yo puedo verificar si una tabla existe o no 
#cursor.execute("SELECT * FROM contacts;")
#contacts = cursor.fetchall()
#print(contacts)  # Muestra todos los contactos en la tabla
#if not contacts:
#    print("No hay contactos en la tabla")

#2 comparador diferente de (!=) nos sirve para comparar si dos valores son diferentes
#Lo usamos para seleccionar registros donde el valor de una columna no es igual a un valor específico

#cursor.execute("SELECT * FROM contacts WHERE != 'Cris'")
#print(cursor.fetchall())  # Devuelve todos los contactos que no tienen el nombre "Cris"

#3 comparador mayor que (>) nos sirve para comparar si un valor es mayor que otro
#cursor.execute("SELECT * FROM contacts WHERE id > 2")
#print(cursor.fetchall())  # Devuelve todos los contactos con un ID mayor que 2

#3.1 comparador mayor o igual que (>=) nos sirve para comparar si un valor es mayor o igual que otro
#cursor.execute("SELECT * FROM contacts WHERE id >= 2")
#print(cursor.fetchall())  # Devuelve todos los contactos con un ID mayor o igual que 2

#4 comparador menor que (<) nos sirve para comparar si un valor es menor que otro
#cursor.execute("SELECT * FROM contacts WHERE id < 2")
#print(cursor.fetchall())  # Devuelve todos los contactos con un ID menor que 2

#4.1 comparador menor o igual que (<=) nos sirve para comparar si un valor es menor o igual que otro
#cursor.execute("SELECT * FROM contacts WHERE id <= 2")
#print(cursor.fetchall())  # Devuelve todos los contactos con un ID menor o igual que 2

#5 comparador LIKE nos sirve para comparar si un valor coincide con un patrón específico
#cursor.execute("SELECT * FROM contacts WHERE name LIKE 'Paula_%'")

#print(cursor.fetchall())

#se utiliza ____ para buscar un patrón específico en una cadena de texto de cantidad de letras
#cursor.execute("SELECT * FROM contacts WHERE name LIKE '____'")

#print(cursor.fetchall())

#Para buscar un nombre que contenga estas letras en cualquier parte del nombre
#cursor.execute("SELECT * FROM contacts WHERE name LIKE '%era%'")

#% es un comodín que representa cero o más caracteres
#Esto significa que estamos buscando contactos cuyos nombres comienzan con "Cris"
#_ es otro comodín que representa un solo carácter
#Por ejemplo, si queremos buscar contactos cuyos nombres comienzan con "Cris" y tienen
#un carácter adicional después de "Cris", usaríamos "Cris_"

#print(cursor.fetchall())  # Devuelve todos los contactos cuyos nombres comienzan con "PaulaTheRevolution"

#6 comparador IN nos sirve para comparar si un valor está dentro de un conjunto de valores

#cursor.execute("SELECT * FROM contacts WHERE name IN ('Cris','Paula')")
#print(cursor.fetchall())  # Devuelve todos los contactos cuyos nombres son "Cris" o "Delvis"

#7 comparador BETWEEN nos sirve para comparar si un valor está dentro de un rango específico
#cursor.execute("SELECT * FROM contacts WHERE id BETWEEN 1 AND 3")
#print(cursor.fetchall())

#8 comparador IS NULL nos sirve para comparar si un valor es nulo
#cursor.execute("SELECT * FROM contacts WHERE email IS NULL")
#print(cursor.fetchall())