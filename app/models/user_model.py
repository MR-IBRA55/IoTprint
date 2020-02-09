from bson import ObjectId
from mongoengine import Document, EmailField, ObjectIdField, StringField


class UserModel(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)
    email = EmailField(required=True, unique=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    meta = {"collection": "users"}

    @classmethod
    def register_user(cls, **kwargs):
        UserModel(**kwargs).save()

    @classmethod
    def get_user_by_id(cls, _id: ObjectId) -> "UserModel":
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
