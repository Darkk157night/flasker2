from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user = User.query.filter_by(username =username_to_check.data).first()
        if user:
            raise ValidationError('Username exists, please choose a new username')

    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email exists try again with new one')
    username = StringField(label='Username: ',validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email: ',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='enter a password: ',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='confirm password: ',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='submit')
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase item')
class SellItemForm(FlaskForm):
    submit = SubmitField(label='sell item')