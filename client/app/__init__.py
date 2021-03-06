import os

from app.views import website_bp
from config import Configs
from flask import Flask

app = Flask(__name__)
app.root_path = os.getenv('ROOT_PATH')
app.template_folder = "app/templates"
app.static_folder = "app/static"
app.config.from_object(Configs)

app.register_blueprint(website_bp)
