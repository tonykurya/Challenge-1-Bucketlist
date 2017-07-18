from flask import Flask, render_template, flash, request, url_for
from content_management import Content


BUCKET_DICT = Content()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            # flash(attempted_username)
            # flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. Try Again."

        return render_template('login.html', error=error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


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
