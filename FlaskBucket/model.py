# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask Class Encapsulating Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, request, flash, redirect
import DataHandler


class FlaskBucket:
    """FlaskBucket Class"""

    def __init__(self, DataHandler):
        self.app = Flask(__name__)
        self.DataHandler = DataHandler

    def register(self):
        """Render register template"""
        if request.method == 'POST':
            username = request.form['Username']
            password = request.form['Password']

            if len(username) == 0:
                flash('Please enter a Username')
            elif len(username) or len(password) < 5:
                flash('Username or Password must have at least 5 characters')
            else:
                DataHandler.USER_DICT[username] = password
                flash('Thanks for registering')
                return redirect(url_for('login'))
        return render_template('register.html')

    def login(self):
        """Render login template"""
        try:
            if request.method == "POST":
                username = request.form['Username']
                password = request.form['Password']

                if len(username) == 0:
                    flash('Please enter a Username')
                elif len(username) or len(password) < 5:
                    flash('Invalid credentials. Try Again.')
                elif username in DataHandler.USER_DICT.key() and password == DataHandler.USER_DICT[username]:
                    return redirect(url_for('home'))
                else:
                    flash("Invalid credentials. Try Again.")

            return render_template('login.html')
        except Exception as e:
            flash(e)
            return render_template('home.html')

    def create(self):
        """Render login template"""
        data = request.form['Text']
        if len(data) == 0:
            flash('Please enter a value')
        elif len(data) > 100:
            flash('Max 100 Characters')
        else:
            DataHandler.BUCKET_LIST.append(data)

        return render_template('view.html')


    def view(self):
        "Render view template"
        return render_template('view.html')

    def home(self):
        """Render home.html"""
        return render_template('home.html')

    def logout(self):
        """Render login.html"""
        return render_template
