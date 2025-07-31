import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import database

auth_bp = Blueprint('auth', __name__)

#Definir nuestros endpoints:

#Creamos nuestro endpoint de registro
@auth_bp.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  email = data.get('email')
  password = data.get('password')
  username = data.get('username')
  
  if not email or not password:
    return jsonify({"error": "Faltan datos"}), 400
  
  if database.create_user(email, username, password):
    return jsonify({"message": "Usuario Registrado con exito"}), 201
  else:
    return jsonify({"error": "El usuario ya existe"}), 400
  
#Creamos nuestro endpoint de login
@auth_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email = data.get('email')
  password = data.get('password')
  
  user_id = database.verify_user(email, password)
  
  #Si tengo mi user_id
  if user_id:
    token = create_access_token(identity=str(user_id), expires_delta=datetime.timedelta(seconds=3600))
    
    #si yo quisiera guardar informacion adicional en el token
    #token = create_access_token(identity=str(user_id), expires_delta=datetime.timedelta(seconds=60), additional_claims={"role": "admin"})
    return jsonify({"token": token}), 200
  return jsonify({"error": "Credenciales incorrectas"}), 401