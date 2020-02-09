from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_mongoengine import MongoEngine
from config import Configs


app = Flask(__name__)
app.config.from_object(Configs)
api = Api(app)
db = MongoEngine(app)
ma = Marshmallow(app)


from app.resources.user_resource import UserRegister, UserLogin, UserProfile
from app.resources.sketch_resource import SketchUpload

api.add_resource(UserRegister, "/api/register")
api.add_resource(UserLogin, "/api/login")
api.add_resource(UserProfile, "/api/profile/<string:_id>")

api.add_resource(SketchUpload, "/api/upload")
