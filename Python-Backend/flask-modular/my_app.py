from flask import Flask
from blueprints.products_bp import products_blueprint
from blueprints.users_bp import users_blueprint

app = Flask(__name__)

#Necesitamos registrar ese blueprint en nuestra aplicacion

app.register_blueprint(products_blueprint, url_prefix='/products')
app.register_blueprint(users_blueprint, url_prefix='/users')

if __name__ == '__main__':
    # Ejecutamos nuestra aplicacion
    app.run(debug=True)