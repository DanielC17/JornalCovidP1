class Estados():
    def __init__(self, nome_estado, sigla, url_imagem):
        self.__nome_estado = nome_estado 
        self.__sigla = sigla 
        self.__url_imagem = url_imagem

    def get_nome_estado(self):
        return self.__nome_estado

    def get_sigla(self):
        return self.__sigla

    def get_url_imagem(self):
        return self.__url_imagem
    
    def set_nome_estado(self, nome_estado):
        self.__nome_estado = nome_estado

    def set_sigla(self, sigla):
        self.__sigla = sigla

    def set_url_imagem(self, url_imagem):
        self.__url_imagem = url_imagem
