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


