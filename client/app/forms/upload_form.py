from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    display_name = StringField(
        "displayName",
        validators=[DataRequired(message="Display name cannot be left plank")],
    )
    file = FileField(
        "file",
        validators=[
            FileRequired(),
            FileAllowed(["gcode"], message="Only gcode files are allowed"),
        ],
    )
