from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    image_file = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp'], 'Only imnages are allowed to be sent')])