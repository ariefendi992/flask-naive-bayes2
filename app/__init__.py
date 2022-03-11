from flask import Flask
from settings import Config
from app.register import registerApp, registerTemplateFilter


def createApp(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)
    registerApp(app)
    registerTemplateFilter(app)
    registerExtensions(app)

    return app


def registerExtensions(app):
    from app.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)
