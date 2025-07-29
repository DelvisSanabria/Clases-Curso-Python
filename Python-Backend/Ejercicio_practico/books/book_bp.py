from flask import Blueprint, request, jsonify
from database import create_connection

bp = Blueprint('books', __name__, url_prefix='/books')

def book_to_dict(book):
    return dict(id=book['id'], 
                tittle=book['tittle'],
                author=book['author'],
                publish_year=book['publish_year'])

@bp.route('/', methods=['GET'])
def get_books():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return jsonify([book_to_dict(book) for book in books])

@bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
    book = cursor.fetchone()
    conn.close()
    
    if book:
        return jsonify(book_to_dict(book))
    return jsonify({'error': 'Libro no encontrado'}), 404

@bp.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    
    # Validación básica
    if not data or 'tittle' not in data or 'author' not in data:
        return jsonify({'error': 'Faltan campos obligatorios (titulo, autor)'}), 400
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO books (tittle, author, publish_year) VALUES (?, ?, ?)',
        (data['tittle'], data['author'], data.get('publish_year'))
    )
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    
    return jsonify({'id': book_id, 'mensaje': 'Libro creado'}), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    
    # Verificar existencia
    cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': 'Libro no encontrado'}), 404
    
    # Actualizar
    cursor.execute(
        '''UPDATE books 
        SET tittle = ?, author = ?, publish_year = ?
        WHERE id = ?''',
        (data.get('tittle'), data.get('author'), 
         data.get('publish_year'), id)
    )
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Libro actualizado'})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Verificar existencia
    cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': 'Libro no encontrado'}), 404
    
    # Eliminar
    cursor.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Libro eliminado'})