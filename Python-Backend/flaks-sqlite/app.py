from flask import Flask
from contacts_bp import contacts_blueprint
from database import initialize_db

app = Flask(__name__)

initialize_db()

app.register_blueprint(contacts_blueprint, url_prefix='/contacts')


if __name__ == '__main__':
    # Ejecutamos nuestra aplicacion
    app.run(debug=True)