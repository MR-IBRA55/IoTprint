from marshmallow import ValidationError

from flask_restful import Resource
from flask import request

from app.models.user_model import UserModel
from app.schemas import UserSchema


class UserRegister(Resource):
    def post(self):
        try:
            requested_data = request.get_json()
            user_schema = UserSchema()
            result: dict = user_schema.load(requested_data)
            UserModel.register_user(**result)
        except ValidationError as err:
            return err.messages
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
        user = UserModel.get_user_by_username(username)
        if user:
            user_schema = UserSchema(only=("first_name", "last_name", "email"))
            result = user_schema.dump(user)
            return result, 200
        return {"msg": "User Not found"}, 404
