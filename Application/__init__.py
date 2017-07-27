'''
from flask import Flask

# Construct an instance of Flask class for the Application
app = Flask(__name__, instance_relative_config=True)

from Application import FlaskBucket


app.config['SECRET_KEY'] = 'secret'
'''
