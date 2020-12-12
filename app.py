from flask import Flask
from views.index import Index
from views.iniciarSesion import IniciarSesion

app = Flask(__name__)

app.register_blueprint(IniciarSesion)
app.register_blueprint(Index)
