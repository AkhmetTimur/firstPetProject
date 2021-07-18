from flask import Flask
from fp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    #create admin user---------------
    from fp.models import User
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            hashed_password=bcrypt.generate_password_hash(app.config['PASSWORD']).decode('utf-8')
            email = app.config['EMAIL']
            admin_user = User(username='admin',email=email,password=hashed_password, is_admin=True)
            db.create_all()
            db.session.add(admin_user)
            db.session.commit()
    #---------------------------------
    
    from fp.main.routes import main
    from fp.user.routes import user
    from fp.admin.routes import admin
    from fp.weight.routes import weight
    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(admin)
    app.register_blueprint(weight)

    #to use "{% continue %} " in templates
    app.jinja_env.add_extension('jinja2.ext.loopcontrols') 
    
    return app