# coding=utf8


import app
from app import db

def create_tables():
    db.create_all(app=app)

create_tables()
