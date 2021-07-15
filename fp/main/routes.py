from flask import Blueprint
from flask import render_template, redirect, url_for
from fp.main.forms import PostForm
from fp.models import Post
from fp import db

main = Blueprint('main',__name__)

@main.route('/', methods=["GET","POST"])
def index():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('index.html', posts=posts, form=form)