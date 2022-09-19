from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from HelloFlask import app


@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    msg = request.args.get("message", None)
    return f"Hello {'World' if name is None else name}!{'' if msg is None else ' ' + msg}"