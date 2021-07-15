from flask import Flask
from fp.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    from fp.main.routes import main
    app.register_blueprint(main)
    
    return app