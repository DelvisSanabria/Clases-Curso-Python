from flask import Flask
from books.book_bp import bp as books_bp
from database import init_db

app = Flask(__name__)

# Inicializar base de datos
init_db()

# Registrar Blueprint
app.register_blueprint(books_bp, url_prefix='/books')

if __name__ == '__main__':
    app.run(debug=True)