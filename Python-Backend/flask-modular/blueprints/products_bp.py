from flask import Blueprint, jsonify

#Creo mi blueprint para los productos que tendra un nombre unico y apuntara a el archivo donde fue creado utilizando __name__
products_blueprint = Blueprint('products_bp', __name__)

# Simulated product data
products_db = [
    {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics"},
    {"id": 3, "name": "Coffee Maker", "price": 150, "category": "Home Appliances"},
    {"id": 4, "name": "Blender", "price": 100, "category": "Home Appliances"},
    {"id": 5, "name": "Headphones", "price": 200, "category": "Electronics"},
]

# Definimos una ruta para obtener todos los productos utilizando el decorador @my_blueprint.route
@products_blueprint.route("/")
def get_product():
  return jsonify(products_db)

@products_blueprint.route("/<int:product_id>")
def get_product_by_id(product_id):
  # Buscamos el producto por su ID
  product = next((p for p in products_db if p["id"] == product_id), None)
  if product:
    return jsonify(product)
  else:
    return jsonify({"error": "Product not found"}), 404