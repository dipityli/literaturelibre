import os

import sqlalchemy
from cs50 import SQL 
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import urllib.parse
from functools import wraps

app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def apology(message, code=400):
    def escape(s):

        for old, new in [("-", "--"), ("-", " "), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

db = SQL("sqlite:///database.db")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/about')
def about():
    return render_template('about-us.html') 

# @app.route('/predict')
# def predict():
#     return render_template('predict.html')
    
# @app.route('/predict_form_inputs', methods=['POST'])
# def predict_form_inputs():
#     return render_template('predict.html', output=output)

# @app.route('/privacy-policy')
# def privacy_policy():
#     return render_template('privacy-policy.html')

def errorhandler(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)