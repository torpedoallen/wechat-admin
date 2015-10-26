# coding=utf8


app_id = ''
secret = ''


if os.path.exists('local_config.py'):
    from .local_config import *
