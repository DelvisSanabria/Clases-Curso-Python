from flask import Flask, jsonify
from auth import auth_bp
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required
import database
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

database.init_db()

# Configuración de JWT usando variables de entorno
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))

jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/protected')
@jwt_required()
def protected():
  user_id = get_jwt_identity()
  #Si tuviera informacion adicional en el token me la podria traer aqui
  """ user_data = get_jwt()
  print(user_data["age"]) """
  return jsonify({"message": f"Acceso concedido para el usuario con ID: {user_id}"}), 200

if __name__ == '__main__':
  # Ejecutamos nuestra aplicacion
  app.run(debug=True)