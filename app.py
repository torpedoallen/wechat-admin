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

db = SQLAlchemy(app)

from wechat_admin.views.base import base_mod
app.register_blueprint(base_mod)
