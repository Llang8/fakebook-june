from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Tell our Flask application to use SQLAlchemy and Migrate and LoginManager
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    moment.init_app(app)

    from app.blueprints.blog import bp as blog
    app.register_blueprint(blog)

    from app.blueprints.main import bp as main
    app.register_blueprint(main)

    from app.blueprints.shop import bp as shop
    app.register_blueprint(shop)

    from app.blueprints.authentication import bp as authentication
    app.register_blueprint(authentication)

    with app.app_context():
        # building the rest of the flask application (configurations, additional packages, etc)
        from app.blueprints.main import routes

    return app