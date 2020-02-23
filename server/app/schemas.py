from flask_marshmallow import Schema
from marshmallow import fields, validate


class UserSchema(Schema):
    _id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    username = fields.Str(validate=validate.Length(min=4, max=24))
    password = fields.Str(validate=validate.Length(min=6))
    email = fields.Email()


class SketchSchema(Schema):
    _id = fields.Str()
    display_name = fields.Str(validate=validate.Length(min=3, max=24))
    filename = fields.Str()
    date = fields.DateTime()


class OrderSchema(Schema):
    _id = fields.Str(load_only=True)
    user = fields.Nested(UserSchema, only=("username",))
    sketch = fields.Nested(SketchSchema, only=("display_name",))
    date = fields.DateTime()
    status = fields.Str()
