from logging import log
from flask import Blueprint, render_template, abort, redirect
from flask.helpers import url_for
from flask_login import login_required, current_user
from fp.models import User
from fp import db

admin = Blueprint('admin',__name__)

def administrator(func):
    #checks whether current_user is admin or not, abort 404 if not 
    def wrapper(*args,**kwargs):
        if  current_user.is_admin:
            return func(*args,**kwargs)
        else:
            abort(404)
    # rename wrapper so decorator can work with more than one func
    wrapper.__name__ = func.__name__
    return wrapper

@admin.route('/admin', methods=["GET","POST"])
@login_required
@administrator
def admin_panel():
        users = User.query.all()
        return render_template('admin.html', users = users)

@admin.route('/admin/delete/<int:user_id>')
@login_required
@administrator
def delete_user(user_id):
    user = User.query.filter_by(id=int(user_id)).first()
    if user.username == "admin":
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin.admin_panel'))

@admin.route('/admin/makeadmin/<int:user_id>')
@login_required
@administrator
def makeadmin_user(user_id):
    user = User.query.filter_by(id=int(user_id)).first()
    if user.username == "admin" or user.id==current_user.id:
        abort(404)
    flag = not(user.is_admin)
    user.is_admin = flag
    db.session.commit()
    return redirect(url_for('admin.admin_panel'))




