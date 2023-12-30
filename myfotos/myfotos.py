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

accounts = {
    "test@example.com": {
        "name": "Teste da Silva",
        "user": "admin",
        "password": "123456789",
        "online": False
    },
    "petunia@example.com": {
        "name": "Petúnia Dias",
        "user": "user",
        "password": "987654321",
        "online": False
    }
}

def valid_login(login, password):
    if login in accounts and accounts[login]["password"] == password:
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

        return f"Bem Vindo {accounts[request.form['login']]["name"]}!"
    
    # if method Get

    return render_template('login.html',
                           login='', error='')

@app.route("/")
def home():
   return render_template('home.html')