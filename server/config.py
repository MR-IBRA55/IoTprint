import os


class Configs(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    MONGODB_SETTINGS = {
        "db": os.getenv("DB"),
        "host": os.getenv("MONGO_HOST"),
        }
