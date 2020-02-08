from typing import Dict
from mongoengine import Document, StringField, EmailField

from app import mongo


class UserModel(Document):
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)
    email = EmailField(required=True, unique=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    @classmethod
    def register_user(cls, email, first_name, last_name, username, password) -> None:
        UserModel(first_name=first_name, last_name=last_name, email=email, username=username, password=password).save()

    @classmethod
    def get_user_by_username(cls, username: str) -> Dict:
        return mongo.db.users.find_one({"username": username})
