from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired("Username cannot be left plank"),
            Length(
                min=4,
                max=24,
                message="Please choose a name between 4 and 24 characters",
            ),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired("Password cannot be left plank"),
            Length(min=6, max=64, message="Password must be more than 6 characters"),
        ],
    )
