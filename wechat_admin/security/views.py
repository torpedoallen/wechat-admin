# coding=utf8

import flask.ext.login as flask_login
from flask import Blueprint, render_template

from app import app
from wechat_admin.security.models import User


security = Blueprint(
    '/security',
    __name__,
    url_prefix='/security',
    template_folder='templates')


@security.route('/login')
def login():
    return render_template('login.html')


@security.route('/logout')
def logout():
    return render_template('logout.html')


@security.route('/register')
def register():
    return render_template('register_user.html')


login_manager = flask_login.LoginManager()
login_manager.login_view = "/security/login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
