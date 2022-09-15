from flask_wtf import FlaskForm
from wtforms import (PasswordField, SelectMultipleField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from app.db_models import Role

class RoleForm(FlaskForm):
	name = StringField("Nome: ", validators=[DataRequired()])
	submit = SubmitField("Salvar")

class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Senha", validators=[DataRequired()])
	submit = SubmitField("Entrar")

class RegisterForm(FlaskForm):
    first_name = StringField("Nome:", validators=[DataRequired(), Length(max=50)])
    last_name = StringField("Sobrenome:", validators=[DataRequired(), Length(max=50)])
    phone = StringField("Telefone:", validators=[DataRequired(), Length(max=30)])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Senha:", validators=[DataRequired(), Regexp("^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message='A senha deve ter 8 caracteres e deve conter letras, números e símbolos.')])
    confirm = PasswordField("Confirmar Senha:",validators=[EqualTo('password', message='As senhas devem corresponder')])
    roles = SelectMultipleField("Funcão:", coerce=int)
    submit = SubmitField("Cadastrar")
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.roles.choices = [(roles.id, roles.name) for roles in Role.query.all()]
