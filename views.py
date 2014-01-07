from flask import Flask ,render_template
import os
from wtforms import Form, BooleanField, TextField, PasswordField, validators


from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired
class MyForm(Form):
    name = TextField('name', validators=[DataRequired()])
    last = TextField('last', validators=[DataRequired()])
    passwd = PasswordField('passwd', validators=[DataRequired()])
 