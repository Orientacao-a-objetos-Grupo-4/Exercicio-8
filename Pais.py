class Pais:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__estados = []
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
    
    def addestado(self, estado):
        self.__estados.append(estado)
    def remestado(self, estado):
        self.__estados.remove(estado)