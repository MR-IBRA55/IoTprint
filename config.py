from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Configs(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    PROPAGATE_EXCEPTIONS = True
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    MONGODB_SETTINGS = {
        'db': os.getenv("DB"),
        'host': os.getenv("MONGO_URI"),
        }
