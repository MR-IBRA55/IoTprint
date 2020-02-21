import os


class Configs(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True
