from flask import Flask

# Construct an instance of Flask class for the Application
app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = 'secret'
