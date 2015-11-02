# coding=utf8

import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from app import db

db.create_all()
db.session.commit()
