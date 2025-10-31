class Filial:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__empresa = None
        self.__cidade = None
        self.__coordenador = None
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome

    def getempresa(self):
        return self.__empresa
    def setempresa(self, empresa):
        self.__empresa = empresa

    def getcidade(self):
        return self.__cidade
    def setcidade(self, cidade):
        self.__cidade = cidade
    
    def getcoordenador(self):
        return self.__coordenador
    def setcoordenador(self, coordenador):
        self.__coordenador = coordenador

    def nome_diretor_empresa(self):
        return self.getempresa().getdiretor().getnome()