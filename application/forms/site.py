# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class ProductForm(Form):
    """Form for product order"""
    email = StringField('')
    phone = PasswordField('')
    id = StringField('')
    '''
    def validate_email(self, field):
        user = User.query.filter(User.email == self.email.data).first()
        if not user:
            raise ValueError("Account doesn't exist.")

    def validate_phone(self, field):
        if self.email.data:
            user = User.query.filter(User.email == self.email.data).first()
            if not user or not user.check_password(self.password.data):
                raise ValueError('Password is not correct.')
            else:
                self.user = user
    '''
class SaleForm(Form):
    """Form for product order"""
    email = StringField('')
    phone = PasswordField('')
    id = StringField('')