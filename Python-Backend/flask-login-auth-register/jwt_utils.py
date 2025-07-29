import jwt
import datetime
from flask import current_app

print(current_app.config['SECRET_KEY'])

#Generar el token
def generate_token(user_id):
  payload = {
    'sub': user_id,
    'exp': datetime.datetime.now() + datetime.timedelta(seconds=3600),
    'iat': datetime.datetime.now()
  }
  return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

#verificar el token

def verify_token(token):
  try:
    payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    return payload['sub']
  except jwt.ExpiredSignatureError:
    return "Token expirado"
  except jwt.InvalidTokenError:
    return "Token"