# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, flash, request, redirect, session, logging
# from passlib.hash import sha256_crypt
from functools import wraps
from account_manager import User
# from wtforms import Form, StringField, validators, PasswordField
import os

app = Flask(__name__)

app.secret_key = os.urandom(20)

global user_accounts
user_accounts = {}

user = User()

# Bucketlist Form Class
'''
class BucketlistForm(Form):
    def __init__(self, title, body):
        title = StringField('Title', [validators.Length(min=1, max=100)])
        body = StringField('Username', [validators.Length(min=4, max=25)])


class RegisterForm(Form):
    def __init__(self, name, username, email, password, confirm):
        username = StringField('Username', [validators.Length(min=4, max=25)])
        email = StringField('Email', [validators.Length(min=6, max=20)])
        password = PasswordField('Password', [validators.DataRequired(),
            validators.EqualTo('confirm', message='Passwords do not match')
        ])
        confirm = PasswordField('Confirm Password')
'''


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        email = request.form['Email']
        username = request.form['Username']
        # password = sha256_crypt.encrypt(str(request.form['Password']))
        password = str(request.form['Password'])

        global user_accounts
        user_accounts[email] = [email, username, password]
        # user_account = User.register(email, username, password)
        # print(user_account)
        return redirect(url_for('login'))
    '''
    if not user_account:
        return render_template('register.html')
    '''

# user login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        global user_accounts
        email_candidate = request.form['Email']
        password_candidate = request.form['Password']

        print(email_candidate)
        print(password_candidate)
        # Get user by email
        print(user_accounts)
        for value in user_accounts.keys():
            print(1)
            if email_candidate == value:
                print(2)
                user_info = user_accounts[email_candidate]
            # Compare Passwords
            # if sha256_crypt.verify(password_candidate, user_password):
                if password_candidate == user_info[-1]:
                    print(3)
                    session['email_candidate'] = True
                    return redirect('/view')

                else:
                    print("We are here")
                    app.logger.info('Invalid password')

            else:
                print("I am here")
                app.logger.info = 'User not found'

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
    form = BucketlistForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        user_id = session['email']
        bucketlist_dict[user_id] = [title, body, user_id]

        flash('Event Created', 'success')

        return redirect(url_for('view'))
    else:
        return render_template('add_bucket_item', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out')


@app.route('/bucket', methods=['GET', 'POST'])
def bucket():
    if request.method == 'GET':
        return render_template('bucket.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'GET':
        return render_template('view.html')


@app.route('/bucket', methods=['GET', 'POST'])
def create_bucketlist():
    # Create Bucketlist
    if request.method == 'POST':
        bucketlist_name = request.form['Name']
        user.bucketlist_name = bucketlist_name

        if bucketlist_name in user.bucketlist_holder.keys():
            flash('That Bucketlist exists, chose another name.')

        else:
            user.add_bucketlist_to_holder(bucketlist_name)
    return render_template('bucket.html')

'''
@app.route('/bucket, methods=['GET', 'POST'])
def add_event():
    # Add Event to Bucketlist
    if request.method == 'POST':
        bucketlist_id = request.form('BucketName')
        if bucketlist_id in user.bucketlist_holder.keys():
            bucket = user.bucketlist_dict[bucketlist_id]
            event = request.form['Event']
            bucket.append(event)


@app.route('view/delete_event')
def delete_event():
    # Delete Event form Bucketlist
    if request.method == 'POST':
        bucketlist_id = request.form['BucketName']
        if bucketlist_id in user
'''

if __name__ == '__main__':
    app.run(debug=True)
