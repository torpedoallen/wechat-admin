# coding=utf8

from flask import Blueprint, render_template


security = Blueprint(
    '/security',
    __name__,
    url_prefix='/security',
    template_folder='wechat_admin/security/templates')


@security.route('/login')
def login():
    return render_template('login.html')


@security.route('/logout')
def logout():
    return render_template('logout.html')


@security.route('/register')
def register():
    return render_template('register.html')
