# coding=utf8

import os

app_id = ''
secret = ''
token = ''
aes_key = ''
auto_replay_text = ''

db_hostname = '0.0.0.0'
db_port = '3306'
db_username = 'root'
db_password = 'root'
db_name = 'wechat_admin'


if os.path.exists('local_config.py'):
    from local_config import *
