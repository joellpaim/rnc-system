from flask_wtf import FlaskForm
from wtforms import (PasswordField, SelectMultipleField, StringField,
                     SubmitField, SelectField, RadioField, TextAreaField, DateField, FileField, widgets)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from app.db_models import Role, User

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
    cod_planta = StringField("1 - Código Planta", validators=[DataRequired(), Length(max=50)])
    nome_cliente = StringField("2 - Nome Cliente", validators=[DataRequired(), Length(max=50)])
    segmento = StringField("3 - Segmento", validators=[DataRequired(), Length(max=50)])
    cod_peca = StringField("4 - Código da Peça", validators=[DataRequired(), Length(max=50)])
    descricao_peca = StringField("5 - Descrição da Peça", validators=[DataRequired(), Length(max=50)])
    linha = StringField("6 - Linha", validators=[DataRequired(), Length(max=50)])
    area = StringField("7 - Área", validators=[DataRequired(), Length(max=50)])
    # Row 2
    procedencia = RadioField('8 - Procedência', choices=[('value','Externa Formal  '),('value_two','Externa Informal  '),('value_tree','Interno')])
    doc_cliente = StringField("Documento Cliente", validators=[DataRequired(), Length(max=50)])
    # Row 3 
    problema_reincidente = RadioField("9 - Problema Reincidente", choices=[('value', 'Não  '), ('value_two', 'Sim  ')])
    ha_devolucao = RadioField("10 - Houve Peça Devolvida", choices=[('value', 'Não  '), ('value_two', 'Sim  ')])
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
    gerar_tratativa = RadioField("18 - Gerar Tratativa?", choices=[('value', 'Não  '), ('value_two', 'Sim  ')])
    pq_nao_tratativa = StringField("Motivo", validators=[DataRequired(), Length(max=250)])
    pos_vendas = StringField("Pós Vendas", validators=[DataRequired(), Length(max=50)])
    #data_registro = DateField("Data", format="%d-%m-%Y")
    visto = MultiCheckboxField("Visto", choices=[('value','Aprovado')])
    anexo = FileField("Anexo")
    salvar_1 = SubmitField("Salvar")

class FaseTwoForm(FlaskForm):
    ct = StringField("CT", validators=[DataRequired(), Length(max=50)])
    area = StringField("Área", validators=[DataRequired(), Length(max=50)])
    exame_objeto = TextAreaField("Examine o objeto", validators=[DataRequired(), Length(max=250)])
    fatos_e_dados = TextAreaField("Checar fatos e dados", validators=[DataRequired(), Length(max=250)])
    compare_com_teoria = TextAreaField("Compare com a teoria", validators=[DataRequired(), Length(max=250)])
    ha_padrao = RadioField("Há padrão dispinível?", choices=[('sim', 'Sim'), ('nao', 'Não')])
    qual_padrao = TextAreaField("Qual?", validators=[DataRequired(), Length(max=250)])
    esta_sendo_seguido = RadioField("Está sendo seguido?", choices=[('sim', 'Sim'), ('nao', 'Não')])
    reclamacao_procedente = RadioField("Reclamação procedente?", choices=[('sim', 'Sim'), ('nao', 'Não')])
    rps = RadioField("Caso sim", choices=[('value', '8D  '), ('value_two', 'Fast Kaizen')])
    rpn = TextAreaField("Atualizar informação", validators=[DataRequired(), Length(max=250)])
    bloquear_embarque = RadioField("Bloquear Embarque", choices=[('sim', 'Sim'), ('nao', 'Não')])
    msg_bloqueio = TextAreaField("Mensagem", validators=[DataRequired(), Length(max=250)])
    imagem_pos = FileField("Anexar Imagem Padrão")
    imagem_neg = FileField("Anexar Imagem Defeito")
    medidas_contencao = TextAreaField("Medidadas de contenção", validators=[DataRequired(), Length(max=250)])
    nome_coordenador = StringField("Nome")
    visto_2 = StringField("Visto")
    data_registro_2 = DateField("Data", format="%d-%m-%Y")
    visto = MultiCheckboxField("Visto", choices=[('value','Aprovado'), ('value2','Reprovado')])
    anexo_2 = FileField("Anexo")
    salvar_2 = SubmitField("Salvar")

class FaseTreeForm(FlaskForm):
    qtd_inspecionada = StringField("Quantidade de inspecionadas?", validators=[DataRequired(), Length(max=50)])
    qtd_reprovadas = StringField("Quantidade de reprovadas", validators=[DataRequired(), Length(max=50)])
    destino = RadioField("Destino", choices=[('desvio', 'Desvio  '), ('sucateamento', 'Sucateamento')])
    texto_destino = TextAreaField("Texto de destino", validators=[DataRequired(), Length(max=250)])
    equipe = MultiCheckboxField("Membros da equipe:", coerce=int)
    data_registro_3 = DateField("Data", format="%d-%m-%Y")
    anexo_3 = FileField("Anexo") 
    salvar_3 = SubmitField("Salvar")
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.equipe.choices = [(user.id, user.first_name) for user in User.query.all()]

class FaseFourForm(FlaskForm):
    mao_de_obra = StringField('Mão de obra ou Pessoas')
    medida = StringField('Medida')
    maquina = StringField('Máquina ou Equipamento')
    materiais = StringField('Materiais')
    meio_ambiente = StringField('Meio Ambiente')
    metodo = StringField('Método')   

    what = StringField('What?')
    why = StringField('Why?')
    where = StringField('Where?')
    when = StringField('When?')
    who = StringField('Who?')
    how_much = StringField('How much?')

    auditoria_escalonada = RadioField("É necessário realizar Auditoria Escalonada?", choices=[('nao', 'Não'), ('sim', 'Sim')])
    numero_auditorias = StringField('Numero')

    linha = SelectField("Qual a linha geradora da não conformidade?", coerce=str)
    
    causa_um = TextAreaField("1", validators=[DataRequired(), Length(max=250)])
    causa_dois = TextAreaField("2", validators=[DataRequired(), Length(max=250)])
    causa_tres = TextAreaField("3", validators=[DataRequired(), Length(max=250)])

    coordenador_rnc = StringField('Coordenador da RNC')
    data_registro_4 = DateField("Data", format="%d-%m-%Y")
    visto_4 = MultiCheckboxField("Visto", choices=[('value','Aprovado'), ('value2','Reprovado')])
    anexo_4 = FileField("Anexo") 

    salvar_4 = SubmitField("Salvar") 

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.linha.choices = ["Agricola", "Média", "Pesada"]
