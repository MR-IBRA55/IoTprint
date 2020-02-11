from flask import Flask
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from app.routes import api_bp
from website.routes import website_bp
from config import Configs

app = Flask(__name__)
app.config.from_object(Configs)
MongoEngine(app)
Marshmallow(app)

app.register_blueprint(website_bp)
app.register_blueprint(api_bp, url_prefix='/api')

