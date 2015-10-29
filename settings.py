# coding=utf8

import os

app_id = ''
secret = ''
token = ''
aes_key = ''
auto_replay_text = ''

db_hostname = 'localhost'
db_port = '3306'
db_username = 'root'
db_password = 'root'
db_name = 'wechat_admin'

menu = {}
click_menu_text_mapper = {}
qiniu_domain_mapper = {}

if os.path.exists('local_settings.py'):
    from local_settings import *
