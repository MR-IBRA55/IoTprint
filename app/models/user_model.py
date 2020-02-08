from mongoengine import Document, StringField, EmailField


class UserModel(Document):
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
    def get_user_by_username(cls, username):
        for user in UserModel.objects(username=username):
            return user
