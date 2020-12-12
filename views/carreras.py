from flask import render_template, Blueprint

Carreras = Blueprint('/carreras', __name__)

@Carreras.route("/carreras")
def carreras():
    return render_template("carreras.html")