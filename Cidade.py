class Cidade:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__estado = None

    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome

    def getestado(self):
        return self.__estado
    def setestado(self, estado):
        self.__estado = estado