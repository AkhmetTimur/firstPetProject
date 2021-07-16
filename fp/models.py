from flask_login.mixins import UserMixin
from fp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=True,unique=True)
    password = db.Column(db.String(60),nullable=True)
    email = db.Column(db.String(120),nullable=True,unique=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return  f"User('{self.username}','{self.email}')"



class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return self.content