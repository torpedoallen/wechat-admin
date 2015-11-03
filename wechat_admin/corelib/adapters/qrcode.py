# coding=utf8


import cStringIO
from wechat_sdk import WechatBasic

import settings
from wechat_admin.corelib.adapters import auth as _wechat

from wechat_admin.vendors.qiniu import proxy as qiniu
from wechat_admin.base.models import Qrcode


class WechatQrcodeAdapter(object):

    @classmethod
    def create_qrcode(cls, name):
        token, expired_at = _wechat.get_access_token()
        wechat = WechatBasic(
            appid=settings.APP_ID,
            appsecret=settings.SECRET,
            access_token=token,
            access_token_expires_at=expired_at)
        payload = {
            "action_name": "QR_LIMIT_STR_SCENE",
            "action_info": {"scene": {"scene_str": name}}}
        resp = wechat.create_qrcode(payload)
        ticket = resp.get('ticket', '')
        url = resp.get('url', '')
        data = cls.show_qrcode(ticket)
        if not data:
            raise
        output = cStringIO.StringIO()
        output.write(data)

        # upload
        p = qiniu.PutPolicy(settings.BUCKET)
        path = '/qrcode/%s' % name
        path, hash_key = p.upload(output, path)
        output.close()

        Qrcode.create_code(name, ticket, url, path, hash_key)
        p = qiniu.PublicGetPolicy(settings.BUCKET, path)
        return p.get_url()

    @classmethod
    def show_qrcode(cls, ticket):
        wechat = WechatBasic(appid=settings.APP_ID, appsecret=settings.SECRET)
        resp = wechat.show_qrcode(ticket)
        if resp.status_code == 200:
            return resp.content

    @classmethod
    def show_all_qrcodes(cls):
        # wtf
        for code in Qrcode.query.all():
            ret = cls.show_qrcode(code.ticket)
            yield code.username, ret
