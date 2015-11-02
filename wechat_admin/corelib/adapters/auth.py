# coding=utf8


import time
import random
import datetime
import settings
from wechat_sdk import WechatBasic
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

TOKEN_KEY = 'wx_at'
TOKEN_EXPIRED_AT_KEY = 'wx_atet'
TICKET_KEY = 'wx_tk'
TICKET_EXPIRED_AT_KEY = 'wx_tket'


def get_access_token():
    token = cache.get(TOKEN_KEY)
    token_expired_at = cache.get(TOKEN_EXPIRED_AT_KEY)
    if token:
        return token, token_expired_at
    b = WechatBasic(
        appid=settings.APP_ID,
        appsecret=settings.SECRET)
    print 'get_access_token at:', datetime.datetime.now()
    d = b.get_access_token()
    token = d['access_token']
    expired_at = d['access_token_expires_at']
    cache.set(TOKEN_KEY, token, (expired_at - time.time())*60)
    cache.set(TOKEN_EXPIRED_AT_KEY, expired_at, (expired_at - time.time())*60)
    return token, expired_at


def get_jsapi_ticket():
    ticket = cache.get(TICKET_KEY)
    expired_at = cache.get(TICKET_EXPIRED_AT_KEY)
    if ticket:
        return ticket, expired_at

    token, expired_at = get_access_token()
    b = WechatBasic(
        appid=settings.APP_ID,
        appsecret=settings.SECRET,
        access_token=token,
        access_token_expires_at=expired_at)

    print 'get_ticket at:', datetime.datetime.now()
    d = b.get_jsapi_ticket()

    ticket = d['jsapi_ticket']
    expired_at = d['jsapi_ticket_expires_at']

    cache.set(TICKET_KEY, ticket, (expired_at - time.time())*60)
    cache.set(TICKET_EXPIRED_AT_KEY, expired_at, (expired_at - time.time())*60)
    return ticket, expired_at


def generate_jsapi_signature(url):

    ticket, expired_at = get_jsapi_ticket()

    b = WechatBasic(
        appid=settings.APP_ID,
        appsecret=settings.SECRET,
        jsapi_ticket=ticket,
        jsapi_ticket_expires_at=expired_at)

    timestamp = int(round(time.time()))
    nonce = random.randint(10000000, 99999999)
    print 'generate signature at:', datetime.datetime.now()
    signature = b.generate_jsapi_signature(
        timestamp, nonce, url, jsapi_ticket=ticket)

    return {
        'appId': settings.APP_ID,
        'timestamp': timestamp,
        'nonceStr': nonce,
        'signature': signature,
    }
