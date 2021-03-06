from typing import List

from app.models.orders_model import OrderModel
from app.models.sketch_model import SketchModel
from app.models.user_model import UserModel
from app.schemas import OrderSchema
from flask import request
from flask_restful import Resource


class OrderCreate(Resource):
    def post(self):
        headers = request.headers
        requested_data = request.get_json()
        user = UserModel.get_user_by_id(headers["User"])
        if user:
            sketch = SketchModel.get_sketch_by_id(requested_data["sketch"])
            if sketch:
                OrderModel.create_order(user, sketch)
                return {"msg": "Order created"}, 201
            return {"msg": "Sketch not found"}, 404
        return {"msg": "User not found"}, 404


class Orders(Resource):
    def get(self):
        orders: List[OrderModel] = OrderModel.get_all_orders()
        if orders:
            schema = OrderSchema(many=True)
            result: dict = schema.dump(orders)
            return result, 200
        return {"msg": "No orders found"}, 404


class Order(Resource):
    def get(self, user_id: str):
        user = UserModel.get_user_by_id(user_id)
        if user:
            schema = OrderSchema(many=True)
            orders: List[OrderModel] = OrderModel.get_orders_by_user(user)
            result = schema.dump(orders)
            return result, 200
        return {"msg": "No user found"}, 404
