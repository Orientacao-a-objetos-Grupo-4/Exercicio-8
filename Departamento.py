class Departamento:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__chefe = None
        self.__empresa = None
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome

    def getchefe(self):
        return self.__chefe
    def setchefe(self, chefe):
        self.__chefe = chefe

    def getempresa(self):
        return self.__empresa
    def setempresa(self, empresa):
        self.__empresa = empresa

    def escolaridade_chefe(self):
        return self.getchefe().getescolaridade().getdescricao()