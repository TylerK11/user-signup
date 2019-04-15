from flask import Flask, redirect, render_template, request
import cgi
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__)
app.config['DEBUG'] = True

def check_username_password(entry):
    if entry == "":
        return False
    elif " " in entry:
        return False
    elif len(entry) < 3 or len(entry) > 20:
        return False
    return True

def check_verify(entry, other_entry):
    if entry == other_entry:
        return True
    return False

def check_email(entry):
    at = "@"
    period = "."
    if entry == '':
        return True
    elif entry.count(at) != 1 or entry.count(period) != 1:
        return False
    return True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def validate_submission():
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    #username validation section
    username = request.form['username']
    if check_username_password(username) == True:
        username = username
    else:
        username_error = "Please Resubmit: Username must not be empty and be between 3 and 20 characters and contain no spaces"

    #password validation section
    password = request.form['password']
    if check_username_password(password) == True:
        password = password
    else:
        password_error = "Please Resubmit: Password must not be empty and be between 3 and 20 characters and contain no spaces"

    #verifying password section
    verify = request.form['verify']
    if check_verify(verify, password) == True:
        verify = verify
    else:
        verify_error = "Passwords do not match, check what you typed"

    #verifying email section
    email = request.form['email']
    if check_email(email) == True:
        email = email
    else:
        email_error = "Not a valid email address"

    if check_username_password(username) == True and check_username_password(password) == True and check_verify(verify, password) == True and check_email(email) == True:
        return render_template('submitted.html', username=username)
    elif check_username_password(username) == False or check_username_password(password) == False or check_verify(verify, password) == False or check_email(email) == False:
        return render_template('index.html', username=username,email=email, email_error=email_error, verify_error=verify_error, username_error=username_error, password_error=password_error)

app.run()