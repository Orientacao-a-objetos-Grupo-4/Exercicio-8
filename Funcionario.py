class Funcionario:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__matricula = None
        self.__cpf = None
        self.__departamento = None
        self.__escolaridade = None
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
    
    def getmatricula(self):
        return self.__matricula
    def setmatricula(self, matricula):
        self.__matricula = matricula
    
    def getcpf(self):
        return self.__cpf
    def setcpf(self, cpf):
        self.__cpf = cpf
    
    def getdepartamento(self):
        return self.__departamento
    def setdepartamento(self, departamento):
        self.__departamento = departamento

    def getescolaridade(self):
        return self.__escolaridade
    def setescolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    def pais_alocacao(self):
        return self.getdepartamento().getempresa().getgrupo().getsede().getnome()
    
    def estado_filial_coordenador(self, filiais):
        for filial in filiais:
            if filial.getcoordenador() is not None:
                if filial.getcoordenador().getid() == self.getid():
                    return filial.getcidade().getestado()
        return None