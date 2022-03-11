from flask import Flask
from settings import Config
from app.register import registerApp, registerTemplateFilter


def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    registerApp(app)
    registerTemplateFilter(app)
    registerExtensions(app)

    return app


def registerExtensions(app):
    from app.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)


app = createApp()
