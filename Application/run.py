# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, flash, request, redirect, session, logging
# from passlib.hash import sha256_crypt
from functools import wraps
from bucket_manager import BucketClass, User
# from wtforms import Form, StringField, validators, PasswordField
import os

import uuid

app = Flask(__name__)

app.secret_key = os.urandom(20)

global user_accounts
user_accounts = {}

user = User()

Buckets = []


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        user.email = request.form['Email']
        user.username = request.form['Username']
        # password = sha256_crypt.encrypt(str(request.form['Password']))
        user.password = str(request.form['Password'])
        # user_account = User.register(email, username, password)
        # print(user_account)
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        email = request.form['Email']
        password = request.form['Password']

        # Get user by email

        if email == user.email and password == user.password:
            # Compare Passwords
            # if sha256_crypt.verify(password_candidate, user_password):
            session['email'] = True
            return redirect(url_for('index'))

        else:
            flash("Wrong email or password", "danger")

    return render_template('login.html')


# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            print('I am here')
            flash('Unauthorized, Please login', 'danger')
            return render_template('view.html')
    return wrap


@app.route('/view', methods=['GET', 'POST'])
@is_logged_in
def view():
    if request.method == 'POST':
        print('bucket')
        bucket_name = request.form['BucketName']
        _id = str(uuid.uuid4())
        Bucket = BucketClass(bucket_name, _id)
        Buckets.append(Bucket)
        print("this is bucket",Buckets)
        return redirect(url_for('view'))
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)
