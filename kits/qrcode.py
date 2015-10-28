# coding=utf8


import settings
from wechat_sdk import WechatBasic
import wechat_wrapper as _wechat


class WechatQrcodeAdapter(object):

    @classmethod
    def create_qrcode(cls, name):
        token, expired_at = _wechat.get_access_token()
        wechat = WechatBasic(
            appid=settings.app_id,
            appsecret=settings.secret,
            access_token=token,
            access_token_expires_at=expired_at)
        payload = {
            "action_name": "QR_LIMIT_STR_SCENE",
            "action_info": {"scene": {"scene_str": name}}}
        ticket = wechat.create_qrcode(payload)
        Qrcode.create_code(name, ticket)
        return ticket

    @classmethod
    def show_qrcode(cls, ticket):
        #wechat = WechatBasic(appid=settings.app_id, appsecret=settings.secret)
        #return wechat.show_qrcode(ticket)
        return '''{"ticket":"gQH47joAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL2taZ2Z3TVRtNzJXV1Brb3ZhYmJJAAIEZ23sUwMEmm3sUw==","expire_seconds":60,"url":"http:\/\/weixin.qq.com\/q\/kZgfwMTm72WWPkovabbI"}'''
