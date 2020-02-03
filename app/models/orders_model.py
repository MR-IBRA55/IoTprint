# from pprint import pprint
#
# from bson import ObjectId
#
# from app import mongo
#
#
# class OrderModel:
#
#     @classmethod
#     def create_order(cls, user_id, sketch_id):
#         pass
#
#     @classmethod
#     def get_first_order(cls, filename):  # todo only extract the filename from db
#         orders = mongo.orders
#         return orders.find_one({"filename": filename})
#
#     @classmethod
#     def get_orders_by_user(cls, username):
#         orders = mongo.orders
#         return orders.find_one({"user": username})
#
#
# pprint(OrderModel.get_orders_by_user(ObjectId('5e36936a86b05417747b7c15')))
