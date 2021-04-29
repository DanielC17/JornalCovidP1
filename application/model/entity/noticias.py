class Noticias():
    def __init__(self, titulo, url_imagem, data, conteudo):
        self.__titulo = titulo
        self.__url_imagem = imagem
        self.__data = data
        self.__conteudo = conteudo
    

    def get_titulo(self):
        return self.__titulo

    def get_url_imagem(self):
        return self.__url_imagem

    def data(self):
        return self.__data

    def conteudo(self):
        return self.__conteudo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_url_imagem(self, imagem):
        self.__url_imagem = imagem

    def set_data(self, data):
        self.__data = data

    def set_conteudo(conteudo):
        self.__conteudo = conteudo

    
