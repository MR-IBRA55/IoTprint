from flask import Flask
from config import Configs
from app.routes import website_bp

app = Flask(__name__)
app.config.from_object(Configs)

app.register_blueprint(website_bp)
