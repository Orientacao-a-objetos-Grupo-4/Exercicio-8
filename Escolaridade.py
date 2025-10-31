class Escolaridade:
    def __init__(self):
        self.__id = None
        self.__descricao = None
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id

    def getdescricao(self):
        return self.__descricao
    def setdescricao(self, descricao):
        self.__descricao = descricao