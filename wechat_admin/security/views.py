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
