from flask import Flask, render_template, flash, request, url_for, redirect, session, g, abort
# from content_management import Content
import os
import sqlite3

# BUCKET_DICT = Content()

app = Flask(__name__)  # Create the applcation instance :)
app.config.from_object(__name__)  # Load config from this file, run.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'bucketlist.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

# app.config.from_envarr('BUCKETLIST_SETTINGS', silent=True)


def connect_db():
    # Connects to a specfic database
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


def get_db():
    '''Opens a new database connection if there is none yet
    for the current application context.
    '''
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    '''Closes the database at the end of request.'''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


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
