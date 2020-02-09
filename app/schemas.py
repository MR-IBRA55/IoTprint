from marshmallow import Schema, fields


class UserSchema(Schema):
    _id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    username = fields.Str()
    password = fields.Str()
