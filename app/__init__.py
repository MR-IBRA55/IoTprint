from flask import Flask
from flask_restful import Api, Resource
from flask_pymongo import PyMongo

from config import Configs


app = Flask(__name__)
app.config.from_object(Configs)
api = Api(app)
mongo = PyMongo(app)

from app.resources.user_resource import UserRegister

api.add_resource(UserRegister, '/register')
