from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import data_required

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [data_required()])
    password = PasswordField('Password', validators = [data_required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('SignIn')

    