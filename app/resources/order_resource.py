from flask import request
from flask_restful import Resource

from app.models.orders_model import OrderModel
from app.models.sketch_model import SketchModel
from app.models.user_model import UserModel
from app.schemas import OrderSchema


class OrderCreate(Resource):
    def post(self):
        requested_data = request.get_json()
        user_id = UserModel.get_user_by_id(requested_data["user_id"])
        sketch_id = SketchModel.get_sketch_by_id(requested_data["sketch_id"])
        if user_id and sketch_id:
            OrderModel.create_order(user_id, sketch_id)
            return {"msg": "Order created"}, 201
        return {"msg": "Bad request"}, 400


class Orders(Resource):
    def get(self, user_id):
        user = UserModel.get_user_by_id(user_id)
        if user:
            schema = OrderSchema(many=True)
            orders = OrderModel.get_orders_by_user_id(user_id)
            result = schema.dump(orders)
            return result, 200
        return {"msg": "Bad request"}, 400
