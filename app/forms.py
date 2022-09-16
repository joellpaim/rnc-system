from flask_wtf import FlaskForm
from wtforms import (PasswordField, SelectMultipleField, StringField,
                     SubmitField, SelectField, RadioField, TextAreaField, DateField, FileField, widgets)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from app.db_models import Role

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

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
    roles = MultiCheckboxField("Funcão:", coerce=int)
    submit = SubmitField("Cadastrar")
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.roles.choices = [(roles.id, roles.name) for roles in Role.query.all()]

class FaseOneForm(FlaskForm):
    # Row 1
    cod_planta = SelectField("1 - Código Planta", validators=[DataRequired()])
    nome_cliente = SelectField("2 - Nome Cliente", validators=[DataRequired()])
    segmento = SelectField("3 - Segmento")
    cod_peca = SelectField("4 - Código da Peça")
    descricao_peca = SelectField("5 - Descrição da Peça")
    linha = SelectField("6 - Linha")
    area = SelectField("7 - Área")
    # Row 2
    procedencia = RadioField('8 - Procedência', choices=[('value','Externa Formal'),('value_two','Externa Informal'),('value_tree','Interno')])
    doc_cliente = StringField("Documento Cliente", validators=[DataRequired(), Length(max=50)])
    # Row 3 
    problema_reincidente = RadioField("9 - Problema Reincidente", choices=[('value', 'Não'), ('value_two', 'Sim')])
    ha_devolucao = RadioField("10 - Houve Peça Devolvida", choices=[('value', 'Não'), ('value_two', 'Sim')])
    qtd_devolucao = StringField("Quantidade devolvida", validators=[DataRequired(), Length(max=50)])
    # Row 4 
    qual_rnc = TextAreaField("11 - Qual é a não conformidade?", validators=[DataRequired(), Length(max=250)])
    o_que = TextAreaField("12 - O que?", validators=[DataRequired(), Length(max=250)])
    quando = TextAreaField("13 - Quando?", validators=[DataRequired(), Length(max=250)])
    onde = TextAreaField("14 - Onde?", validators=[DataRequired(), Length(max=250)])
    quem = TextAreaField("15 - Quem?", validators=[DataRequired(), Length(max=250)])
    como = TextAreaField("16 - Como foi detectado?", validators=[DataRequired(), Length(max=250)])
    modo_de_falha = TextAreaField("17 - Modo de falha", validators=[DataRequired(), Length(max=250)])
    # Row 5 
    gerar_tratativa = RadioField("18 - Gerar Tratativa?", choices=[('value', 'Não'), ('value_two', 'Sim')])
    pq_nao_tratativa = StringField("Motivo", validators=[DataRequired(), Length(max=250)])
    pos_vendas = SelectField("Pós Vendas")
    data_registro = DateField("Data", format="%d-%m-%Y")
    visto = MultiCheckboxField("Visto", choices=[('value','Aprovado')])
    anexo = FileField("Anexo")
    submit = SubmitField("Salvar")