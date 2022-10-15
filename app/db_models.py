from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the User data-model
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean())
    email = db.Column(db.String(50), nullable=False)
    email_confirmed_at = db.Column(db.DateTime())
    phone = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    # Relationships	
    roles = db.relationship('Role', secondary='user_roles')

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return self.name

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

class RelatorioNC(db.Model):
    __tablename__ = 'rncs'
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return self.code