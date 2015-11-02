# coding=utf8

from webchat_admin import db

class Qrcode(db.Model):

    __bind_key__ = 'wechat_admin'
    __tablename__ = 'qrcode'

    id = db.Column(db.Integer, primary_key=True)
    scene = db.Column(db.String(64), unique=True, index=True)
    ticket = db.Column(db.String(128))
    url = db.Column(db.String(128))
    path = db.Column(db.String(128))
    hash_key = db.Column(db.String(128))

    @classmethod
    def create_code(cls, name, ticket, url, path, hash_key):
        code = cls()
        code.scene = name
        code.ticket = ticket
        code.url = url
        code.path = path
        code.hash_key = hash_key
        db.session.add(code)
        db.session.commit()
        return code
