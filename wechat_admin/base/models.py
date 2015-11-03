# coding=utf8

import datetime
from app import db


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

class SubscribeEvent(db.Model):

    __bind_key__ = 'wechat_admin'
    __tablename__ = 'subscribe_event'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), index=True)
    scene = db.Column(db.String(32), index=True)
    subscribed_at = db.Column(db.DateTime, index=True)

    @classmethod
    def create_event(cls, user_id, scene, subscribed_at):
        event = cls()
        event.user_id = user_id
        event.scene = scene
        event.subscribed_at = datetime.datetime.fromtimestamp(subscribed_at)
        db.session.add(event)
        db.session.commit()
        return event


class UnsubscribeEvent(db.Model):

    __bind_key__ = 'wechat_admin'
    __tablename__ = 'unsubscribe_event'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), index=True)
    unsubscribed_at = db.Column(db.DateTime, index=True)

    @classmethod
    def create_event(cls, user_id, unsubscribed_at):
        event = cls()
        event.user_id = user_id
        event.unsubscribed_at = datetime.datetime.fromtimestamp(unsubscribed_at)
        db.session.add(event)
        db.session.commit()
        return event
