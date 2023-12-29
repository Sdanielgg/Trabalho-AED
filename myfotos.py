#!python
#
# Para correr a app:
# - abrir terminal
# - digitar: flask --debug --app myfotos run
# - copiar o url: http://127.0.0.1:5000 para o browser
#

from flask import Flask
from flask import render_template
from flask import request
import re

app = Flask(__name__)


def valid_login(login, password):
    if login == "test@example.com" and password == "12345678":
        return True

    return False

@app.route("/registo")
def signup():
    return "Registo!"

@app.route("/login",  methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        if not re.match(r"[^@]+@[^@]+\.[^@]+", request.form['login']):
            return render_template('login.html',
                    login=request.form['login'],
                    error="Email incorrecto!")
        
        if len(request.form['password']) < 8:
            return render_template('login.html',
                    login=request.form['login'],
                    error="Password incorrecta!")

        if not valid_login(request.form['login'], request.form['password']):
            return render_template('login.html',
                               login=request.form['login'],
                               error="Password ou login incorrecto!")

        return "Account Created!"
    
    # if method Get

    return render_template('login.html',
                           login='')

@app.route("/")
def home():
   return render_template('home.html')