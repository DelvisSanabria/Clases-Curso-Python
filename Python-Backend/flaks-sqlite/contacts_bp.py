from flask import Blueprint,request, jsonify
from database import get_db_connection
import sqlite3

contacts_blueprint = Blueprint('contacts_bp', __name__)

#Yo quiero crear el CRUD de contactos

#Create (POST): Crear un contacto

@contacts_blueprint.route("/", methods=['POST'])
def create_contact():
  #Obtenemos el JSON enviado desde el cliente
  new_data = request.get_json()
  #Validamos que los datos no esten vacios
  if not new_data or not "name" in new_data or not "phone" in new_data or not "email" in new_data:
    return jsonify({"error": "Faltan datos"}), 400
  
  name = new_data['name']
  phone = new_data['phone']
  email = new_data['email']
  #Para datos opcionales, podemos usar el metodo get
  #address = new_data.get('address', None)
  
  conn = get_db_connection()
  cursor = conn.cursor()
  try:
    cursor.execute('''
      INSERT INTO contacts (name, phone, email)
      VALUES (?, ?, ?)
    ''', (name, phone, email))
    conn.commit()
    new_contact_id = cursor.lastrowid
    return jsonify({"id": new_contact_id, "name": name, "phone": phone, "email": email}), 201
  except sqlite3.IntegrityError as e:
    return jsonify({"error": "El contacto ya existe"}), 400
  finally:
    conn.close()
    
#Read (GET): Obtener todos los contactos
@contacts_blueprint.route("/", methods=['GET'])
def get_contacts():
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM contacts')
  #Creo diccionarios para cada uno de los contactos en la base de datos
  contacts = [dict(contact) for contact in cursor.fetchall()]
  conn.close()
  
  return jsonify(contacts), 200

#Read (GET): Obtener un contacto por ID
@contacts_blueprint.route("/<int:contact_id>", methods=['GET'])
def get_contact(contact_id):
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
  contact = cursor.fetchone()
  conn.close()
  
  if contact is None:
    return jsonify({"error": "Contacto no encontrado"}), 404
  
  return jsonify(dict(contact)), 200

#Update (PATCH): Actualizar un contacto por ID
@contacts_blueprint.route("/<int:contact_id>", methods=['PATCH'])
def update_contact(contact_id):
  #Obtenemos el JSON enviado desde el cliente
  new_data = request.get_json()
  if not new_data:
    return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
  
  #Creamos variables con los datos a actualizar
  name = new_data.get('name')
  phone = new_data.get('phone')
  email = new_data.get('email')
  
  #Nos conectamos a la base de datos
  conn = get_db_connection()
  cursor = conn.cursor()
  
  #Verificar si el usuario existe
  cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
  contact = cursor.fetchone()
  if contact is None:
    conn.close()
    return jsonify({"error": "Contacto no encontrado"}), 404
  
  #Ahora actualizamos los datos
  query_parts = []
  values = []
  
  if name is not None:
    query_parts.append("name = ?")
    values.append(name)
  if phone is not None:
    query_parts.append("phone = ?")
    values.append(phone)
  if email is not None:
    query_parts.append("email = ?")
    values.append(email)
    
  if not query_parts:
    conn.close()
    return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
  
  query = f"UPDATE contacts SET {', '.join(query_parts)} WHERE id = ?"
  values.append(contact_id)
  
  try:
    cursor.execute(query, tuple(values))
    conn.commit()
    cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
    updated_contact = cursor.fetchone()
    conn.close()
    return jsonify(dict(updated_contact)), 200
  except sqlite3.IntegrityError as e:
    conn.close()
    return jsonify({"error": "Error al actualizar el contacto"}), 400
  
#Delete (DELETE): Eliminar un contacto por ID
@contacts_blueprint.route("/<int:contact_id>", methods=['DELETE'])
def delete_contact(contact_id):
  conn = get_db_connection()
  cursor = conn.cursor()
  
  try:
    #Verificar si el contacto existe
    cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
    contact = cursor.fetchone()
    
    if contact is None:
      conn.close()
      return jsonify({"error": "Contacto no encontrado"}), 404
    
    #Eliminar el contacto
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    if cursor.rowcount > 0:
      conn.close()
      return jsonify({"message": "Contacto eliminado exitosamente"}), 200
    else:
      conn.close()
      return jsonify({"error": "Error al eliminar el contacto"}), 500
  except sqlite3.IntegrityError as e:
    conn.close()
    return jsonify({"error": "Error al eliminar el contacto"}), 500
  finally:
    conn.close()