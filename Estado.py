class Estado:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__pais = None
        self.__cidades = []
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome

    def getpais(self):
        return self.__pais
    def setpais(self, pais):
        self.__pais = pais

    def addcidade(self, cidade):
        self.__cidades.append(cidade)
    def remcidade(self, cidade):
        self.__cidades.remove(cidade)