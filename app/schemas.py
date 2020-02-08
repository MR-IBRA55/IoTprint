from marshmallow import Schema, fields


class UserSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    username = fields.Str()
    password = fields.Str()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)
