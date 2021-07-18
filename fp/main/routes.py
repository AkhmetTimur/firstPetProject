from flask import Blueprint
from flask import render_template, redirect, url_for
from fp.main.forms import PostForm
from fp import db



main = Blueprint('main',__name__)

@main.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')