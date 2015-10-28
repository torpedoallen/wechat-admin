# coding=utf8


import config
from wechat_sdk import WechatBasic


class WechatMenuAdapter(object):

    @classmethod
    def get_menus(cls):
        token = config.token
        wechat = WechatBasic(token=token)
        return wechat.get_menu()
