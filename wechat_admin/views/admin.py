

from flask import request, Blueprint, render_template, redirect
from flask.ext.security import login_required


admin = Blueprint('/admin', __name__, url_prefix='/admin')


# Views
@admin.route('/')
@login_required
def home():
    return render_template('index.html')


@admin.route('/login')
def login():
    callback = request.args.get('next', '/')
    return redirect(callback, code=302)
