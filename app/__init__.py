from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    manager.add_command('db', MigrateCommand)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app