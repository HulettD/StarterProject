from flask import Flask
from os.path import join, dirname, realpath


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' # TODO: Secret key stuffs (required for flash)
# Trick from stackoverflow to generate the absolute path since the relative path was not working as demonstrated in the flask tutorial
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static/uploads')
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

import HelloFlask.views