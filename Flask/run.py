# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask webapp to Create Read Update Delete BucketList
"""
from flask import Flask, render_template, url_for, request, flash, redirect


USER_DICT = {}


# Construct an instance of Flask class for the Application
app = Flask(__name__, static_url_path='/static')
app.debug = True  # Enable reloader and debugger
app.secret_key = 'TTTT'


@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Render register template"""
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']
        USER_DICT[username] = password
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render login template"""
    error = ''
    try:
        if request.method == "POST":
            username = request.form['Username']
            password = request.form['Password']

            if username in USER_DICT.key() and password == USER_DICT[username]:
                return redirect(url_for('home'))
            else:
                error = "Invalid credentials. Try Again."

        return render_template('login.html', error=error)
    except Exception as e:
        flash(e)
        return render_template('home.html', error=error)


@app.route('/home')
def home():
    """Render home.html"""
    return render_template('home.html')


if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run()  # Launch built-in web server and run this Flask webapp
