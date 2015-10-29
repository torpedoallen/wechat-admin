# coding=utf8


import settings
from wechat_sdk import WechatBasic


class WechatMenuAdapter(object):

    @classmethod
    def create_menu(cls, data):
        wechat = WechatBasic(appid=settings.app_id, appsecret=settings.secret)
        resp = wechat.create_menu(data)
        return resp.get('errmsg', '')
