#!python
#
# Para correr a app:
# - abrir terminal
# - digitar: flask --debug --app myfotos run
# - copiar o url: http://127.0.0.1:5000 para o browser
#

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/registo")
def signup():
    return "Registo!"

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
def home():
   return render_template('home.html')