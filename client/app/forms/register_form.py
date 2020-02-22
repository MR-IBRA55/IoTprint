from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    first_name = StringField("firstName")
    last_name = StringField("lastName")
    email = EmailField(
        "email", validators=[DataRequired(message="Email cannot be left plank")]
    )
    username = StringField(
        "username",
        validators=[
            DataRequired(message="Username cannot be left plank"),
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
            DataRequired(message="Password can not be left plank"),
            Length(min=6, max=64, message="Password must be more than 6 characters"),
        ],
    )
