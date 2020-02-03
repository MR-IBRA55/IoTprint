from app import mongo
from flask import jsonify


class UserModel:

    @classmethod
    def register_user(cls, username, password, email):
        data = {"username": username,
                "password": password,
                "email": email
                }
        mongo.db.users.insert_one(data)

    @classmethod
    def get_user_by_username(cls, username):
        users = mongo.users
        return users.find_one({"username": username})
