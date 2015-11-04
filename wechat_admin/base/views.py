# coding=utf8


import settings

from flask import request, Blueprint

from wechat_sdk import WechatBasic
from wechat_sdk.messages import EventMessage

from wechat_admin.base.models import SubscribeEvent, UnsubscribeEvent
from wechat_admin.corelib.adapters.menu import WechatMenuAdapter
from wechat_admin.corelib.adapters.qrcode import WechatQrcodeAdapter

base = Blueprint('/', __name__)


@base.route('/', methods=['POST', 'GET'])
def index():
    token = settings.TOKEN
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
        response = wechat.group_transfer_message()
    elif message.type == 'image':
        response = wechat.response_text(u'图片')
    elif isinstance(message, EventMessage):
        if message.type == 'subscribe':
            if message.key and message.ticket:
                scene = message.key.startswith(
                    'qrscene_') and message.key[8:] or 'default'
            else:
                scene = 'default'

            SubscribeEvent.create_event(message.source, scene, message.time)
            response = wechat.response_text(content=settings.GREETINGS)

        elif message.type == 'unsubscribe':
            UnsubscribeEvent.create_event(message.source, message.time)
            # TODO
            response = ''
        elif message.type == 'scan':
            # TODO
            response = ''
        elif message.type == 'location':
            response = wechat.response_text(content=u'上报地理位置事件')
        elif message.type == 'click':
            content = settings.CLICK_MENU_TEXT_MAPPER.get(message.key, u'未知')
            response = wechat.response_text(content=content)
        elif message.type == 'view':
            response = wechat.response_text(content=u'自定义菜单跳转链接事件')
        elif message.type == 'templatesendjobfinish':
            response = wechat.response_text(content=u'模板消息事件')
    else:
        response = wechat.response_text(u'未知')
    return response


# TODO: to post
@base.route('/menus', methods=['GET'])
def create_menu():
    message = WechatMenuAdapter.create_menu(settings.MENU)
    return message


# TODO: to post
@base.route('/qrcodes', methods=['GET'])
def create_qrcode():
    name = request.args.get('name', '')
    url = WechatQrcodeAdapter.create_qrcode(name)
    return url


@base.route('/show_qrcodes', methods=['GET'])
def show_qrcode():
    ret = list(WechatQrcodeAdapter.show_all_qrcodes())
    return str(ret)
