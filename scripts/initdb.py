# coding=utf8

import os
import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from wechat_admin import db

print db

db.create_all()
db.session.commit()
