from flask import Flask, redirect, render_template, request
import cgi
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__)
app.config['DEBUG'] = True

def check_username(entry):
    if entry == "":
        return False
    elif " " in entry:
        return False
    elif len(entry) > 3 or len(entry) < 20:
        return False
    return True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def validate_submission():
    username = request.form['username']
    if check_username(username) == True:
        return render_template('submitted.html', username=username)
    else:
        error = "Please resubmit"
        return render_template('index.html', username_error=error)

app.run()