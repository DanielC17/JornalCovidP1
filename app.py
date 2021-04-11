
from flask import Flask, render_template, 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Alo mundão!'



app . run ( debug = True )   # recarregar na aplicação com o debug.