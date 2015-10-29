# coding=utf8

import settings
from flask import request, Flask

from flask.ext.sqlalchemy import SQLAlchemy

from wechat_sdk import WechatBasic
from wechat_sdk.messages import EventMessage

from kits.menu import WechatMenuAdapter
from kits.qrcode import WechatQrcodeAdapter


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

app.config['TOKEN'] = settings.token
app.config['SQLALCHEMY_DATABASE_URI'] = db_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_BINDS'] = db_binds

db = SQLAlchemy(app)


# models
class Qrcode(db.Model):

    __bind_key__ = 'wechat_admin'
    __tablename__ = 'qrcode'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    ticket = db.Column(db.String(128))
    url = db.Column(db.String(128))

    @classmethod
    def create_code(cls, name, ticket, url):
        code = cls()
        code.username = name
        code.ticket = ticket
        code.url = url
        db.session.add(code)
        db.session.commit()
        return code


@app.route('/', methods=['POST', 'GET'])
def index():
    token = app.config['TOKEN']
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')

    # 实例化 wechat
    wechat = WechatBasic(token=token)

    if not wechat.check_signature(signature=signature,
                                  timestamp=timestamp, nonce=nonce):
        return 'fail'

    # 对签名进行校验
    echostr = request.args.get('echostr')
    if echostr:
        return echostr

    wechat.parse_data(request.data)
    message = wechat.get_message()
    if message.type == 'text':
        response = wechat.response_text(settings.auto_replay_text)
    elif message.type == 'image':
        response = wechat.response_text(u'图片')
    elif isinstance(message, EventMessage):
        if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
            if message.key and message.ticket:  # 如果 key 和 ticket 均不为空，则是扫描二维码造成的关注事件
                response = wechat.response_text(content=u'用户尚未关注时的二维码扫描关注事件')
            else:
                response = wechat.response_text(content=u'普通关注事件')
        elif message.type == 'unsubscribe':
            response = wechat.response_text(content=u'取消关注事件')
        elif message.type == 'scan':
            response = wechat.response_text(content=u'用户已关注时的二维码扫描事件')
        elif message.type == 'location':
            response = wechat.response_text(content=u'上报地理位置事件')
        elif message.type == 'click':
            content = settings.click_menu_text_mapper.get(message.key, u'未知')
            response = wechat.response_text(content=content)
        elif message.type == 'view':
            response = wechat.response_text(content=u'自定义菜单跳转链接事件')
        elif message.type == 'templatesendjobfinish':
            response = wechat.response_text(content=u'模板消息事件')
    else:
        response = wechat.response_text(u'未知')
    return response


# TODO: to post
@app.route('/menus', methods=['GET'])
def create_menu():
    message = WechatMenuAdapter.create_menu(settings.menu)
    return message


# TODO: to post
@app.route('/qrcodes', methods=['GET'])
def create_qrcode():
    name = request.args.get('name', '')
    ticket = WechatQrcodeAdapter.create_qrcode(name)
    return ticket

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998, debug=True)
