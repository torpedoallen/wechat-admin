# coding=utf8


from app import db


class Qrcode(db.Model):

    __bind_key__ = 'wechat_admin'
    __tablename__ = 'qrcode'

    username = db.Column(db.String(64), unique=True)
    ticket = db.Column(db.String(128))
    url = db.Column(db.String(128))
