from flask import Flask, jsonify
from auth import auth_bp, token_required
import database


app = Flask(__name__)

app.config['SECRET_KEY'] = 'super_secret_key'

app.register_blueprint(auth_bp, url_prefix='/auth')