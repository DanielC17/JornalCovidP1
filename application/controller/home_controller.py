from application import app
from flask import render_template, request, url_for
from application.model.dao.estadosDao import EstadosDAO
from application.model.entity.estados import Estados
from application.model.entity.noticias import Noticias
from application import lista_noticias
from application import lista_estados


@app.route("/")
def index():
    estadosDAO = EstadosDAO()
    return render_template("index.html", lista_estados = estadosDAO.get_lista_estados())

@app.route('/<titulo>')
def noticias(titulo):
    for noticias in lista_noticias:
        if noticias.get_titulo() == titulo:
            return render_template("noticias.html", noticias = noticias)
    return render_template("index.html", lista_estados = lista_estados)
