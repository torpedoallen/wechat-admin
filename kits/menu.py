# coding=utf8


import settings
from wechat_sdk import WechatBasic


class WechatMenuAdapter(object):

    @classmethod
    def get_menus(cls):
        #wechat = WechatBasic(appid=settings.app_id, appsecret=settings.secret)
        #d = wechat.get_access_token()
        #wechat = WechatBasic(appid=settings.app_id, appsecret=settings.secret, access_token=d['access_token'], access_token_expires_at=d['access_token_expires_at'])
        #return wechat.get_menu()
        return '''{"menu":{"button":[{"type":"click","name":"今日歌曲","key":"V1001_TODAY_MUSIC","sub_button":[]},{"type":"click","name":"歌手简介","key":"V1001_TODAY_SINGER","sub_button":[]},{"name":"菜单","sub_button":[{"type":"view","name":"搜索","url":"http://www.soso.com/","sub_button":[]},{"type":"view","name":"视频","url":"http://v.qq.com/","sub_button":[]},{"type":"click","name":"赞一下我们","key":"V1001_GOOD","sub_button":[]}]}]}}'''
