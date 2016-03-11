# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Login form to access writing and settings pages"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])