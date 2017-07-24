# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, request, flash, request, redirect, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from Application import app
from passlib.hash import sha256_crypt
from functools import wraps


user_dict = {}
registered_emails = []
bucketlist_dict = {}


# Bucketlist Data Class
class Bucketlist(object):
    def __init__(self, name, email):
        self.data = {}
        self.name = name
        self.email = email


# Bucketlist Form Class
class BucketlistForm(Form):
    title = StringField('Title', [validators.length(min=1, max=100)])
    body = StringField('Username', [validators.Length(min=4, max=25)])


class RegisterForm(object):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=20)])
    password = PasswordField('Password', [validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate() is True:
        name=form.name.data
        email=form.email.data
        username=form.username.data
        password=sha256_crypt.encrypt(str(form.password.data))

        if email in user_dict:
            flash('That email is already registered')

        else:
            user_dict[email]=[name, username, email, password]
            flash('Welcome to Bucketlist')
            redirect(url_for('login')
    # return render_template('register.html', form=form)


# user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username=request.form['Email']
        password_candidate=request.form['Password']

        # Get user by email
        result=user_dict[email]

        if len(result) > 0:
            # Get stored hash
            # Get this information from list
            password=result[3]

        # Compare Passwords
        if sha256_crypt.verify(password_candidate, password)
            app.logger.info('PASSWORD MATCHED')

        else:
            app.logger.info('PASSWORD NOT MATCHED')

    else:
        error='User not found'


    return render_template('login.html')


# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/add_item', methods=['GET', 'POST'])
@is_logged_in
def add_bucket_item():
    form=BucketlistForm(request.form)
    if request.method == 'POST' and form.validate():
        title=form.title.data
        body=form.body.data

        user_id=session['email']
        bucketlist_dict[user_id]=[title, body, user_id]

        flash('Event Created', 'success')

        return redirect(url_for('view')
    return render_template('add_bucket_item', form=form)


@app.route('/view', methods=['GET', 'POST'])
def view():
    if len(bucketlist_dict) > 0:
        for user, event in bucketlist_dict:
            return render_template('view.html', event=event)
    else:
        msg='No Articles Found'

    return render_template('view.html')


if __name__ == __main__:
    app.run(debug=True)
