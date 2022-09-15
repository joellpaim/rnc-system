from flask import Blueprint, render_template
from ..db_models import db, User
from ..funcs import admin_only



admin = Blueprint("admin", __name__, url_prefix="/admin",
                  static_folder="static", template_folder="templates")


@admin.route('/users')
@admin_only
def users():
    users = User.query.all()
    return render_template("users.html", users=users)