import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from app.routes import api_bp
from config import Configs

app = Flask(__name__)
app.root_path = os.getenv("ROOT_PATH")
app.config.from_object(Configs)
db = MongoEngine()
ma = Marshmallow()
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api_bp, url_prefix="/api")
