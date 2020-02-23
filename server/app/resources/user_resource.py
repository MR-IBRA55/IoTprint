from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.user_model import UserModel
from app.schemas import UserSchema
from secrets import compare_digest


class UserSignUp(Resource):
    def post(self):
        try:
            requested_data = request.get_json()
            if UserModel.get_user_by_username(requested_data["username"]):
                return {"msg": "Username already exists"}, 400
            if UserModel.get_user_by_email(requested_data["email"]):
                return {"msg": "Email already exists"}, 400
            user_schema = UserSchema()
            result: dict = user_schema.load(requested_data)
            UserModel.register_user(**result)
            return {"msg": "Registration successful"}, 201
        except ValidationError as err:
            return jsonify(err.messages, 400)


class UserLogin(Resource):
    def post(self):
        requested_data = request.get_json()
        user = UserModel.get_user_by_username(requested_data["username"])
        if user:
            if compare_digest(requested_data["password"], user.password):
                return {"msg": "Login successful"}, 200
            else:
                return {"msg": "Bad username or password"}, 400
        return {"msg": "Invalid username or password"}, 400


class UserProfile(Resource):
    def get(self, _id: str):
        user = UserModel.get_user_by_id(_id)
        if user:
            user_schema = UserSchema(
                only=("first_name", "last_name", "email", "username")
            )
            result: dict = user_schema.dump(user)
            return result, 200
        return {"msg": "User Not found"}, 404
