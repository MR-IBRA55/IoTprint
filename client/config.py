import os

from dotenv import load_dotenv

load_dotenv()


class Configs(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True
