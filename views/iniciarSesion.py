from flask import Blueprint, render_template

IniciarSesion = Blueprint("/iniciar-sesion", __name__)

@IniciarSesion.route("/iniciar-sesion")
def iniciarSesion():
    render_template("iniciar-sesion.html")