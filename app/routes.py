from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

from app.resources.user_resource import UserRegister, UserLogin, UserProfile
from app.resources.sketch_resource import SketchUpload, Sketches, Sketch
from app.resources.order_resource import OrderCreate, Orders

api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserProfile, "/profile/<string:_id>")

api.add_resource(SketchUpload, "/upload")
api.add_resource(Sketches, "/sketches")
api.add_resource(Sketch, "/sketch/<string:_id>")

api.add_resource(OrderCreate, "/order")
api.add_resource(Orders, "/orders/<string:user_id>")
