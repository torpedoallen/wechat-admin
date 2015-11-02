# coding=utf8

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

APP_ID = ''
SECRET = ''
TOKEN = ''
AES_KEY = ''
GREETINGS = ''
AUTO_REPLAY_TEXT = ''
SECURITY_SECRET = ''

DB_HOSTNAME = 'localhost'
DB_PORT = '3306'
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'wechat_admin'

MENU = {}
CLICK_MENU_TEXT_MAPPER = {}
QINIU_DOMAIN_MAPPER = {}
BUCKET = ''
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''

if os.path.exists('local_settings.py'):
    # pylint: disable=W0401
    from local_settings import *
    # pylint: enable=W0401
