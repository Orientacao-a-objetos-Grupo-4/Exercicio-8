class Grupo:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__presidente = None
        self.__sede = None

    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
    
    def getpresidente(self):
        return self.__presidente
    def setpresidente(self, presidente):
        self.__presidente = presidente

    def getsede(self):
        return self.__sede
    def setsede(self, sede):
        self.__sede = sede
    
    def escolaridadePresidente(self):
        return self.getpresidente().getescolaridade().getdescricao()