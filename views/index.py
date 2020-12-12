from flask import render_template, Blueprint

Index = Blueprint("/", __name__)

@Index.route("/")
def index():
    return render_template("index/index.html")