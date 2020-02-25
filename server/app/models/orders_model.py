from datetime import datetime
from typing import List

from bson import ObjectId
from mongoengine import (DateTimeField, Document, ObjectIdField, ReferenceField, StringField)

from app.models.sketch_model import SketchModel
from app.models.user_model import UserModel


class OrderModel(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    user = ReferenceField(UserModel)
    sketch = ReferenceField(SketchModel)
    date = DateTimeField(default=datetime.utcnow)
    status = StringField(
        default="standby", choices=("standby", "printing", "finished"), required=True
        )
    meta = {"collection": "orders", "ordering": ["-date"]}

    @classmethod
    def create_order(cls, user, sketch) -> None:
        OrderModel(user=user, sketch=sketch).save()

    @classmethod
    def get_orders_by_user(cls, user: "UserModel") -> "List[OrderModel]":
        orders = OrderModel.objects(user=user)
        return orders

    @classmethod
    def get_all_orders(cls) -> "List[OrderModel]":
        orders = OrderModel.objects().exclude('user')
        return orders

    @classmethod
    def change_status(cls):
        pass
