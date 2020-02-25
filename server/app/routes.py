from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

from app.resources.user_resource import UserSignUp, UserLogin, UserProfile
from app.resources.sketch_resource import SketchUpload, Sketches, Sketch
from app.resources.order_resource import OrderCreate, Orders, Order
from app.resources.files_resource import AllFiles, DownloadFile

api.add_resource(UserSignUp, "/signup")
api.add_resource(UserLogin, "/login")
api.add_resource(UserProfile, "/profile/<string:_id>")

api.add_resource(SketchUpload, "/upload")
api.add_resource(Sketches, "/sketches")
api.add_resource(Sketch, "/sketch/<string:_id>")

api.add_resource(OrderCreate, "/order")
api.add_resource(Orders, "/orders")
api.add_resource(Order, "/order/<string:user_id>")

api.add_resource(AllFiles, "/files")
api.add_resource(DownloadFile, "/files/<path:filename>")
