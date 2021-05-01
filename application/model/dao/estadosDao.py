from application.model.entity.estados import Estados
from application import lista_estados

class EstadosDAO():
    
    def __init__(self):
        self.__lista_estados = lista_estados

    def get_lista_estados(self):
        return self.__lista_estados
