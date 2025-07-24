from flask import Flask, request


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
  
#Los parametros que yo defino en la url, deben ser enviados de forma obligatoria o el endpoint no funcionará
@app.route("/ciudad/<string:city>/cp/<int:postal_code>")
def city_info(city, postal_code):
    return f"<h1>¡Hola, estas en el endpoint ciudad!</h1><p>Ciudad: {city}, Código Postal: {postal_code}</p>"
  
#Para parametros opcionales, puedo definir query parameters que se envian de forma opcional

@app.route("/search_products")
def search_products():
  #request.args es un diccionario que contiene los parametros enviados en la url
  #Si no se envian, se puede definir un valor por defecto
  query = request.args.get('q', 'No se ha enviado una consulta')
  
  min_price = request.args.get('min_price', 'No se ha enviado un precio mínimo')
  max_price = request.args.get('max_price', 'No se ha enviado un precio máximo')
  
  return f"<h1>¡Hola, estas en el endpoint de búsqueda de productos!</h1><p>Consulta: {query}</p><p>Precio mínimo: {min_price}</p><p>Precio máximo: {max_price}</p>"
  
if __name__ == '__main__':
    #Ejecutamos nuestra aplicacion
    app.run(debug=True)