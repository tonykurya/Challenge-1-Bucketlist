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
    '''Connects to a specfic database'''
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
    '''Initializes the database.'''
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


@app.route('/show_entries')
def show_entries():
    '''This view shows all the entries stored in the database'''
    db = get_db()
    cur = db.execute('select event from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    '''This view lets the user add new entries if they are logged in.'''
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (event) values (?)',
               [request.form['event']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/register')
def register():
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
