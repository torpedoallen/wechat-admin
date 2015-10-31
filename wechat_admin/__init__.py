# coding=utf8

import datetime
import settings
from flask import request, Flask

from flask.ext.sqlalchemy import SQLAlchemy

from wechat_sdk import WechatBasic
from wechat_sdk.messages import EventMessage

from adapters.menu import WechatMenuAdapter
from adapters.qrcode import WechatQrcodeAdapter


app = Flask(__name__)
db_str = 'mysql://%s:%s@%s:%s/%s' % (
    settings.db_username,
    settings.db_password,
    settings.db_hostname,
    settings.db_port,
    settings.db_name)

db_binds = {
    settings.db_name: db_str,
}


app.config['DEBUG'] = True
app.config['TOKEN'] = settings.token
app.config['SQLALCHEMY_DATABASE_URI'] = db_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_BINDS'] = db_binds

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998,)

