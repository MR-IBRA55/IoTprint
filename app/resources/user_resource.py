from flask_restful import Resource
from flask import request

from app.models.user_model import UserModel


class UserRegister(Resource):
    def post(self):
        requested_data = request.get_json()
        UserModel.register_user(requested_data)
        return {"msg": "Registration successful"}, 201


class UserLogin(Resource):
    def post(self):
        requested_data = request.get_json()
        user = UserModel.get_user_by_username(requested_data["username"])
        if user:
            if requested_data["password"] == user["password"]:
                return {"msg": "Login successful"}, 200
            else:
                return {"msg": "Bad username or password"}, 400
        return {"msg": "Bad username or password"}, 400


class UserProfile(Resource):
    def get(self, username):
        pass
