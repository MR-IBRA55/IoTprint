from flask_restful import Resource
from flask import jsonify, request

from app.models.user_model import UserModel


class UserRegister(Resource):
    def post(self):
        postData = request.get_json()
        username = postData["username"]
        password = postData["password"]
        email = postData["email"]
        UserModel.register_user(username, password, email)

        return jsonify({"message": "Hello, World!"})
