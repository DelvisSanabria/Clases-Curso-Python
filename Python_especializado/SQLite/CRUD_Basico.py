#CRUD se refiere a las operaciones que yo le puedo realizar a mis datos

#Create: Creamos nuevos registros

#Read: Leemos los registros

#Update: Actualizamos los registros

#Delete: Borramos los registros

#Importamos sqlite3 para trabajar con bases de datos SQLite 
import sqlite3
#Establecer la conexion a mi base de datos
conn = sqlite3.connect("./Python_especializado/SQLite/example_DB.db")

#necesitamos llamar a un cursor, que nos permite manipular la base de datos a la que nos conectamos

cursor = conn.cursor()

#para ejecutar comando SQL con mi cursor utilizare el metodo execute

cursor.execute("""INSERT INTO users (username,hashed_password,isDeleted) VALUES (
"DelvisPrime","Cont12345", FALSE
),
(
"CrisPrime","Contrasena15#", TRUE
),
(
"HerasiPrime","Con#trasena1.", FALSE
);""")

#Actualizamos la base de datos y guardamos los cambios
conn.commit()

#Selecciono todos mis usuarios
cursor.execute("SELECT * FROM users")

#Muestro todos los resultados de la consulta anterior en consola
print(cursor.fetchall())

#Cerramos la conexion
conn.close

#Practica

#1. Crear una base de datos llamada "practica.db"
#2. Crear una tabla llamada "users" con las columnas "id", "username", "hashed_password", "isDeleted"
#3.Meterle a users 10 usuarios
#4.mostrar los 10 usuarios de la tabla "users"
