from bson import ObjectId
from mongoengine import Document, EmailField, ObjectIdField, StringField


class UserModel(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    email = EmailField(required=True, unique=True)
    meta = {"collection": "users"}

    @classmethod
    def register_user(cls, **kwargs) -> None:
        UserModel(**kwargs).save()

    @classmethod
    def get_user_by_id(cls, _id: str) -> "UserModel":
        for user in UserModel.objects(_id=_id):
            return user

    @classmethod
    def get_user_by_username(cls, username: str) -> "UserModel":
        for user in UserModel.objects(username=username):
            return user

    @classmethod
    def get_user_by_email(cls, email: str) -> "UserModel":
        for user in UserModel.objects(email=email):
            return user
