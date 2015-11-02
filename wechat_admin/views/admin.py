

from flask import request, Blueprint, render_template, redirect
from flask.ext.security import login_required


admin = Blueprint('/admin', __name__, url_prefix='/admin')

from app import app, db

@app.before_first_request
def create_user():
    db.create_all()
    #user_datastore.create_user(email='matt@nobien.net', password='password')
    print '111'
    #db.session.commit()


# Views
@admin.route('/')
@login_required
def home():
    return render_template('index.html')
