class Empresa:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__diretor = None
        self.__grupo = None

    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome

    def getdiretor(self):
        return self.__diretor
    def setdiretor(self, diretor):
        self.__diretor = diretor
    
    def getgrupo(self):
        return self.__grupo
    def setgrupo(self, grupo):
        self.__grupo = grupo