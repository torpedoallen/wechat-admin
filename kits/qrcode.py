# coding=utf8


import settings


from wechat_sdk import WechatBasic
import wechat_wrapper as _wechat


class WechatQrcodeAdapter(object):

    @classmethod
    def create_qrcode(cls, name):
        from app import Qrcode
        token, expired_at = _wechat.get_access_token()
        wechat = WechatBasic(
            appid=settings.app_id,
            appsecret=settings.secret,
            access_token=token,
            access_token_expires_at=expired_at)
        payload = {
            "action_name": "QR_LIMIT_STR_SCENE",
            "action_info": {"scene": {"scene_str": name}}}
        resp = wechat.create_qrcode(payload)
        ticket = resp.get('ticket', '')
        url = resp.get('url', '')
        Qrcode.create_code(name, ticket, url)
        return url

    @classmethod
    def show_qrcode(cls, ticket):
        wechat = WechatBasic(appid=settings.app_id, appsecret=settings.secret)
        resp = wechat.show_qrcode(ticket)
        if resp.status_code == 200:
            return resp.content

    @classmethod
    def show_all_qrcodes(cls):
        # wtf
        from app import Qrcode
        for code in Qrcode.query.all():
            ret = cls.show_qrcode(code.ticket)
            yield code.username, ret
