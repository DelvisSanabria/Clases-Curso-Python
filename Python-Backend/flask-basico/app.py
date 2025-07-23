from flask import Flask


#Creamos una instancia de Flask para decirle a Flask que este es nuestro archivo principal
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>¡Hola, desde flask!</h1>"
  
@app.route('/usuarios')
def hello_user():
    return "<h1>¡Hola, estas en el endpoint usuarios!</h1>"
  
#Parametros: El nombre de la variable es el mismo que el de la url
@app.route('/usuarios/saludar/<username>')
#Definimos una ruta que recibe un parametro
#y lo usamos para saludar al usuario
def say_hello(username):
    return f"<h1>¡Hola,{username}, estas en el endpoint usuarios!</h1>"
  
if __name__ == '__main__':
    #Ejecutamos nuestra aplicacion
    app.run(debug=True)