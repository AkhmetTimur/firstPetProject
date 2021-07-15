from fp import db

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(40), nullable=False,unique=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.content