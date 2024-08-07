from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.event import event
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(event)

    return app
