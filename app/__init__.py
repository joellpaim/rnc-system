import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_bootstrap import Bootstrap
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from werkzeug.security import check_password_hash, generate_password_hash
from .admin.routes import admin

from .db_models import db, User, Role, UserRoles
from .forms import LoginForm, RegisterForm, RoleForm

# Carregar info do env e registrar o app
load_dotenv()
app = Flask(__name__)
app.register_blueprint(admin)

# Carregar info do env via os
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
# SQLite
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URI"]
# MySQL
user = "root"
password = ""
server = "localhost"
database = "flask"
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+mysqlconnector://{user}:{password}@{server}/{database}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['MYSQL_CHARSET'] = 'utf8mb4'
app.config['MAIL_USERNAME'] = os.environ["EMAIL"]
app.config['MAIL_PASSWORD'] = os.environ["PASSWORD"]
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_PORT'] = 587


Bootstrap(app)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
	db.create_all()

@app.context_processor
def inject_now():
	""" sends datetime to templates as 'now' """
	return {'now': datetime.utcnow()}

@login_manager.user_loader
def load_user(user_id):
    print('Usuario: ', user_id)
    try:
        return User.query.get(user_id)
    except:
        return None

@app.route("/roles", methods=['GET', 'POST'])
def create_roles():
    try:
        form = RoleForm()
        if form.validate_on_submit():
            new_role = Role(name=form.name.data)
            db.session.add(new_role)
            db.session.commit()
            flash('Função cadastrada com sucesso!', 'success')
            return redirect(url_for('create_roles'))
    except Exception as e:
        flash(f'Erro: {e}', 'flash-error')
        return redirect(url_for('create_roles'))

    return render_template("roles.html", form=form)


@app.route("/", methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		user = User.query.filter_by(email=email).first()
		if user == None:
			flash(f'Não existe usuário com email: {email} <br> <a href={url_for("register")}>Cadastrar agora</a>', 'error')
			return redirect(url_for('login'))
		elif check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect(url_for('home'))
		else:
			flash("Email e senha incorretos!!", "error")
			return redirect(url_for('login'))
	return render_template("login.html", form=form)

@app.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash(f"Usuário com email {user.email} já existe!!<br> <a href={url_for('login')}>Entrar agora</a>", "error")
            return redirect(url_for('register'))
        new_user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        active=1,
                        email=form.email.data,
                        email_confirmed_at=datetime.utcnow(),
                        phone=form.phone.data,
                        password=generate_password_hash(
                                    form.password.data,
                                    method='pbkdf2:sha256',
                                    salt_length=8))

        all_roles = Role.query.filter(Role.id.in_(form.roles.data)).all()
        new_user.roles.extend(all_roles)
                        
        db.session.add(new_user)
        db.session.commit()
        # send_confirmation_email(new_user.email)
        flash('Obrigado por seu cadastro! Você deve logar agora.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

	