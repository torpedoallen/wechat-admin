# coding=utf8

import settings

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

db_str = 'mysql://%s:%s@%s:%s/%s' % (
    settings.DB_USERNAME,
    settings.DB_PASSWORD,
    settings.DB_HOSTNAME,
    settings.DB_PORT,
    settings.DB_NAME)

db_binds = {
    settings.DB_NAME: db_str,
}


app.config['DEBUG'] = True
app.config['TOKEN'] = settings.TOKEN
app.config['SQLALCHEMY_DATABASE_URI'] = db_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_BINDS'] = db_binds
app.config['SECRET_KEY'] = settings.SECURITY_SECRET

db = SQLAlchemy(app)

from wechat_admin.views.base import base_mod
from wechat_admin.views.admin import admin
app.register_blueprint(base_mod)
app.register_blueprint(admin)


from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = "/admin/login"
login_manager.init_app(app)

