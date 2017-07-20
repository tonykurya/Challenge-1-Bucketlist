# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, request, flash, redirect
from DataHandler import USER_DICT, BUCKET_LIST


class FlaskBucket:
    """Flask Bucket."""

    def __init__(self, DataHandler):
        self.app = Flask(__name__)
        self.USER_DICT = USER_DICT
        self.BUCKET_LIST = BUCKET_LIST

    def register(self):
        if request.method == 'POST':
            username = request.form['Username']
            password = request.form['Password']

            if len(username) == 0:
                flash('Please enter a Username')
            elif len(username) or len(password) < 5:
                flash('Username or Password must have at least 5 characters')
            else:
                USER_DICT[username] = password
                flash('Thanks for registering')
                return redirect(url_for('login'))
        return render_template('register.html')

    def login(self):
        try:
            if request.method == "POST":
                username = request.form['Username']
                password = request.form['Password']

                if len(username) == 0:
                    flash('Please enter a Username')
                elif len(username) or len(password) < 5:
                    flash('Invalid credentials. Try Again.')
                elif username in USER_DICT.key() and password == USER_DICT[username]:
                    return redirect(url_for('home'))
                else:
                    flash("Invalid credentials. Try Again.")

            return render_template('login.html')
        except Exception as e:
            flash(e)
            return render_template('home.html')

    def create(self):
        data = request.form['Text']
        if len(data) == 0:
            flash('Please enter a value')
        elif len(data) > 100:
            flash('Max 100 Characters')
        else:
            BUCKET_LIST.append(data)

        return render_template('view.html')

    def bucketlist_manipulation(self):
        event = str(request.data.get('Event'))
        boolean_field = str(request.data.get('Boolean'))

        if request.method == 'DELETE' and boolean_field == 'True':
            for val in BUCKET_LIST:
                if request.data.get('Boolean') == 'True':
                    BUCKET_LIST.remove(val)
            return render_template('view.html')

        elif request.method == 'POST':
            BUCKET_LIST.append(event)
            return render_template('view.html')

    def view(self):
        [val for val in BUCKET_LIST]
        return render_template('view.html', val=val)

    def home(self):
        return render_template('home.html')

    def logout(self):
        return render_template
