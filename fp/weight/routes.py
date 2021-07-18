from flask import Blueprint, render_template, redirect, url_for,request
from flask_login import login_required, current_user
from fp.weight.forms import WeightForm
from fp import db
from fp.models import Weight
from datetime import  date




weight = Blueprint('weight',__name__)

@weight.route('/', methods=["GET","POST"])
def index():
    #to add: show all users results
    return render_template('index.html')


@weight.route('/add', methods=["GET","POST"])
@login_required
def add():
    form = WeightForm()
    if form.validate_on_submit():

        new_weight = Weight(weight_date=form.weight_date.data,weight=form.weight.data,user_id=current_user.id)
        db.session.add(new_weight)
        db.session.commit()
        return redirect(url_for('user.profile'))
    elif request.method=="GET":
        form.weight_date.data = date.today()
    return render_template('add_weight.html', form=form)

    
@weight.route('/delete/<int:weight_id>')
@login_required
def delete(weight_id):
    weight = Weight.query.filter_by(id=weight_id).first()
    db.session.delete(weight)
    db.session.commit()
    return redirect(url_for('user.profile'))