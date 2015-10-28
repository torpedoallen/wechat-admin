# coding=utf8

import os

app_id = ''
secret = ''
token = ''
aes_key = ''
auto_replay_text = ''


if os.path.exists('local_config.py'):
    from local_config import *
