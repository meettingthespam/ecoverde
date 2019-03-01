# https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
# you're someweher ^^
# and someweher at cory schafers tutorial nuimber 10

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from FlaskBuild.config import Config



db = SQLAlchemy()
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from FlaskBuild.main.routes import main
    from FlaskBuild.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
