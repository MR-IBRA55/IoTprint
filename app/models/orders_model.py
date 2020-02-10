from datetime import datetime
from typing import List

from bson import ObjectId
from mongoengine import DateTimeField, Document, ObjectIdField, StringField, ReferenceField, ListField

from app.models.sketch_model import SketchModel
from app.models.user_model import UserModel


class OrderModel(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    user_id = ReferenceField(UserModel)
    sketch_id = ReferenceField(SketchModel)
    date = DateTimeField(default=datetime.utcnow)
    status = StringField(default='standby', choices=('standby', 'printing', 'finished'),
                         required=True)
    meta = {"collection": "orders"}

    @classmethod
    def create_order(cls, user_id, sketch_id):
        OrderModel(user_id=user_id, sketch_id=sketch_id).save()

    @classmethod
    def get_first_order(cls, date):
        pass

    @classmethod
    def get_orders_by_user_id(cls, user_id):
        orders = []
        for order in OrderModel.objects(user_id=user_id):
            orders.append(order)
        return orders

    @classmethod
    def change_status(cls):
        pass
