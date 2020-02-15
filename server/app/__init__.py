from flask import Flask
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from app.routes import api_bp
from config import Configs

app = Flask(__name__)
app.config.from_object(Configs)
db = MongoEngine()
ma = Marshmallow(app)

app.register_blueprint(api_bp, url_prefix='/api')
