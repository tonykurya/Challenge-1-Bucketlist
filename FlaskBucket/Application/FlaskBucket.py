# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import render_template, url_for, request, flash, redirect
from Application import app


class Account(object):
    """
    This class represents user account data and methods.
    """

    def __init__(self):
        """
        Initialize self
        """
        self.bucket = []
        self.email = ""
        self.name = ""
        self.password = ""

    def add_event(self, event):
        """
        Method that adds an event to the bucket
        """
        self.bucket.append(event)

    def delete_event(self, event):
        """
        Method that deletes an event from the bucket
        """
        self.bucket.remove(event)


user_blueprint = Account()
user_accounts = []

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', username=user_blueprint.name)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = str(request.form.get('Email'))
        username = str(request.form.get('Username'))
        password = str(request.form.get('Password'))

        try:
            if len(username) == 0:
                flash('Please enter a Username')
            elif len(username) or len(password) < 5:
                flash('Username or Password must have at least 5 characters')
            else:
                user_blueprint.email = email
                user_blueprint.name = username
                user_blueprint.password = password
                user_accounts.append(user_blueprint)
                flash('Thanks for registering')
                return redirect(url_for('home'))
        except Exception as e:
            return render_template('home.html')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = str(request.form.get('Username'))
        password = str(request.form.get('Password'))
        for user in user_accounts:     
            if username == user_blueprint.name and password == user_blueprint.password:
                return redirect(url_for('view'))
            else:
                return redirect(url_for('register'))
    return render_template('login.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        item = str(request.form.get('Item'))
        if item:
            user_blueprint.add_event(item)
    username = user_blueprint.name
    return render_template('view.html', user_bucket=user_blueprint.bucket, username=user_blueprint.name)


@app.route('/view/<event>/delete', methods=['POST'])
def delete_bucket_event(event):
    if event in user_blueprint.bucket:
        user_blueprint.delete_event(event)
    return redirect(url_for('view'))
