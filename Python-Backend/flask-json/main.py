from flask import Flask, request, jsonify, abort

app = Flask(__name__)

#creemos datos simulados para los productos

products_db = {
    1: {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    2: {"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics"},
    3: {"id": 3, "name": "Coffee Maker", "price": 150, "category": "Home Appliances"},
    4: {"id": 4, "name": "Blender", "price": 100, "category": "Home Appliances"},
    5: {"id": 5, "name": "Headphones", "price": 200, "category": "Electronics"},
}

@app.route("/api/products/<int:product_id>")
def get_product(product_id):
  #Obtenemos un producto por su ID
  product = products_db.get(product_id)
  if product:
    #Si el producto existe, lo devolvemos como JSON
    return jsonify(product)
  #Si el producto no existe, devolvemos un error 404
  else:
    #abort nos sirve para lanzar un error 404 con un mensaje personalizado
    abort(404, description="Product not found")
    
@app.route("/api/products")
def get_all_products():
  #Devolvemos todos los productos como JSON
  return jsonify(list(products_db.values()))

#Vamos a personalizar los mensajes de error
@app.errorhandler(404)
def not_found(error):
  return jsonify({"error": "Recurso no encontrado", "message": error.description}), 404

@app.errorhandler(500)
def internal_error(error):
  return jsonify({"error": "Error interno del servidor", "message": str(error)}), 500
    
if __name__ == '__main__':
    #Ejecutamos nuestra aplicacion
    app.run(debug=True)