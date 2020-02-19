from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    displayName = StringField('displayName', validators=[DataRequired()])
    file = FileField(validators=[FileRequired()])
