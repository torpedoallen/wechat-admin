# coding=utf8


import qiniu as _q
import settings

q = _q.Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


class UploadFailedError(Exception):
    pass


class PutPolicy(object):

    def __init__(self, scope):
        self.scope = scope

    def upload(self, data, path):
        token = q.upload_token(self.scope)
        data.seek(0)
        ret, _ = _q.put_data(token, path, data)
        if ret:
            return path, ret['hash']
        raise UploadFailedError


class PrivateGetPolicy(object):

    def __init__(self, scope, path):
        self.scope = scope
        self.path = path

    def get_url(self):
        domain = settings.QINIU_DOMAIN_MAPPER.get(self.scope)
        base_url = '%s/@%s' % (domain, self.path)
        return q.private_download_url(base_url, expires=3600)


class PublicGetPolicy(object):

    def __init__(self, scope, path):
        self.scope = scope
        self.path = path

    def get_url(self):
        domain = settings.QINIU_DOMAIN_MAPPER.get(self.scope)
        return '%s/@%s' % (domain, self.path)
