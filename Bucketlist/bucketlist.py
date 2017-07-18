from flask import Flask, render_template, flash, request, url_for, redirect, session, g, abort
from content_management import Content
import os
import sqlite3

BUCKET_DICT = Content()

app = Flask(__name__) # Create the applcation instance :)
app.config.from_object(__name__) # Load config from this file, run.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'bucket.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envarr('BUCKET_SETTINGS', silent=True)


def connect_db():
    # Connects to a specfic database
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            flash(attempted_username)
            flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. Try Again."

        return render_template('login.html', error=error)

    except Exception as e:
        flash(e)
        '''
    return render_template("login.html")


@app.route('/register')
def createaccount():
    return render_template('register.html')


@app.route('/view')
def view():
    return render_template('view.html', BUCKET_DICT=BUCKET_DICT)


@app.route('/create')
def create():
    return render_template('create.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(405)
def method_not_found(e):
    return render_template('405.html')


if __name__ == '__main__':
    app.run(debug=True)
