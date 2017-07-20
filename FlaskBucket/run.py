# -*- coding: UTF-8 -*-
"""
flaskBucket: Python-Flask webapp to Create Read Update Delete BucketList
"""
from flask import Flask
import FlaskBucket
import Config


# Construct an instance of Flask class for the Application
app = Flask(__name__)
app.debug = True        # Enable reloader and debugger
app.secret_key = Config.SECRETKEY


@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    return FlaskBucket.register


@app.route('/login', methods=['GET', 'POST'])
def login():
    return FlaskBucket.register


@app.route('/create', methods=['POST'])
def create():
    return FlaskBucket.create


@app.route('/view')
def view():
    return FlaskBucket.view


@app.route('/home')
def home():
    return FlaskBucket.home


if __name__ == '__main__':  # Script executed directly (instead of via import)?
    try:
        app.run()  # Launch built-in web server and run this Flask webapp
    except KeyboardInterrupt:
        exit()
