from marshmallow import Schema, fields, validate, post_load

from app.models.orders_model import OrderModel


class UserSchema(Schema):
    _id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    username = fields.Str(validate=validate.Length(min=4, max=24))
    password = fields.Str(validate=validate.Length(min=6))


class SketchSchema(Schema):
    _id = fields.Str()
    display_name = fields.Str(validate=validate.Length(min=3, max=24))
    filename = fields.Str()
    date = fields.DateTime()


class OrderSchema(Schema):
    _id = fields.Str()
    user_id = fields.Str(load_only=True)
    sketch_id = fields.Str(load_only=True)
    date = fields.DateTime()
    status = fields.Str()

