from app.controllers.c_user import users
from app.controllers.c_dashboard import dashboard
from app.controllers.c_beasiswa_utk import ukt
from app.lib.custom_filter_template import tempFilter


def registerApp(app):
    app.register_blueprint(users)
    app.register_blueprint(dashboard)
    app.register_blueprint(ukt)


def registerTemplateFilter(app):
    app.register_blueprint(tempFilter)