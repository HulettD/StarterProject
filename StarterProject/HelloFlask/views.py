from datetime import datetime
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from HelloFlask import app
import os
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


@app.route("/uploads/<path:name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        upload = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if upload.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if upload and allowed_file(upload.filename):
            filename = secure_filename(upload.filename)
            upload.save(
                os.path.join(app.config["UPLOAD_FOLDER"], filename)
            )  # TODO: Add timestamp or something to prevent duplicate names overwriting each other?
            return redirect(url_for("download_file", name=filename))
    return render_template("upload.html", title="Document Storage Prototype")


@app.route("/")
@app.route("/home")
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title="Hello Flask",
        message="Hello, Flask!",
        content=" on " + formatted_now,
    )


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    msg = request.args.get("message", None)
    return (
        f"Hello {'World' if name is None else name}!{'' if msg is None else ' ' + msg}"
    )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/about")
def about():
    return render_template(
        "about.html", title="About HelloFlask", content="Example app page for Flask."
    )
