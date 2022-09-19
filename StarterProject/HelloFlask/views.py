from flask import Flask
from HelloFlask import app
from flask import request

@app.route('/')
@app.route('/home')
def home():
    return "Hello Flask!"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    msg = request.args.get("message", None)
    return f"Hello {'World' if name is None else name}!{'' if msg is None else ' ' + msg}"