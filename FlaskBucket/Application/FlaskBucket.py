# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, request, flash, request, redirect, session, logging
from passlib.hash import sha256_crypt
from functools import wraps
# from account_manager import Bucketlist
import os

app = Flask(__name__)

app.secret_key = os.urandom(20)

user_accounts = {}

'''
# Bucketlist Form Class
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
        email_candidate = request.form['Email']
        password_candidate = request.form['Password']

        # Get user by email
        for value in user_accounts.keys():
            if email_candidate == value:
                user_info = user_accounts[email_candidate]
            # Compare Passwords
            #if sha256_crypt.verify(password_candidate, user_password):
                if password_candidate == user_info[2] and email_candidate == user_info[0]:
                    session['email'] = email_candidate
                    redirect('view.html')

            else:
                app.logger.info('Invalid password')

        else:
            app.logger.info = 'User not found'

    return render_template('login.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('view.html')


'''
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
'''

if __name__ == '__main__':
    app.run(debug=True)
