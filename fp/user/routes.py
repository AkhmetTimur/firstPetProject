from flask import Blueprint, request, render_template, redirect, url_for,current_app
from flask_login import current_user, login_user,  logout_user, login_required
from fp import bcrypt, db
from fp.models import User, Weight
from fp.user.forms import RegisterForm, LoginForm
from fp.user.utils import plot



user = Blueprint('user',__name__)



@user.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form,title="Register")


@user.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if  user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=False)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@user.route('/profile')
@login_required
def profile():
    weights = Weight.query.order_by(Weight.weight_date.desc()).filter_by(user_id=current_user.id).all()
    userdate,userweight=[],[]
    for weight in weights:
        userdate.append(weight.weight_date)
        userweight.append(weight.weight)
    result = plot(current_user.id,userdate,userweight)
    path = url_for('static',filename='images/'+ result)
    return render_template('profile.html', weights=weights,url=path)
        

