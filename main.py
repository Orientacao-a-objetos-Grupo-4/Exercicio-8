from Grupo import Grupo
from Funcionario import Funcionario
from Departamento import Departamento
from Escolaridade import Escolaridade
from Pais import Pais
from Empresa import Empresa
from Filial import Filial
from Estado import Estado
from Cidade import Cidade

dep1 = Departamento()
f1 = Funcionario()
f2 = Funcionario()
f3 = Funcionario()
f4 = Funcionario()
esc1 = Escolaridade()
gp1 = Grupo()
p1 = Pais()
emp1 = Empresa()

p1.setid(1)
p1.setnome("Brasil")

est1 = Estado()
est1.setid(1)
est1.setnome("Minas Gerais")
est1.setpais(p1)

ci1 = Cidade()
ci1.setid(1)
ci1.setnome("Juiz de Fora")
ci1.setestado(est1)

gp1.setid(1)
gp1.setnome("Aliança")
gp1.setsede(p1)

emp1.setid(1)
emp1.setnome("Aliança Perfumes")
emp1.setgrupo(gp1)

dep1.setid(1)
dep1.setnome("Financeiro")
dep1.setempresa(emp1)

esc1.setid(1)
esc1.setdescricao("Ensino Superior Completo")

f1.setid(1)
f1.setnome("João")
f1.setmatricula(123456)
f1.setcpf(11122233345)
f1.setdepartamento(dep1)
f1.setescolaridade(esc1)

f2.setid(2)
f2.setnome("Maria")
f2.setmatricula(65432)
f2.setcpf(99988877765)
f2.setdepartamento(dep1)
f2.setescolaridade(esc1)

f3.setid(3)
f3.setnome("José")
f3.setmatricula(558978)
f3.setcpf(11233455678)
f3.setdepartamento(dep1)
f3.setescolaridade(esc1)

f4.setid(4)
f4.setnome("Alice")
f4.setmatricula(889520)
f4.setcpf(23443211240)
f4.setdepartamento(dep1)
f4.setescolaridade(esc1)

fil1 = Filial()
fil1.setid(1)
fil1.setnome("Jardim")
fil1.setcidade(ci1)
fil1.setempresa(emp1)

fil2 = Filial()
fil2.setid(1)
fil2.setnome("Independencia")
fil2.setcidade(ci1)
fil2.setempresa(emp1)

gp1.setpresidente(f1)
emp1.setdiretor(f2)
fil1.setcoordenador(f3)
dep1.setchefe(f4)


print("_____________________________________________________________________________________")
print("Exercício 1: Qual a escolaridade do presidente de um grupo?")
print(f"A escolaridade do Presidente {gp1.getpresidente().getnome()}, do Grupo {gp1.getnome()}, é {gp1.escolaridadePresidente()}")

print("_____________________________________________________________________________________")
print("Exercício 2: Qual o país de alocação de um funcionário?")
print(f"O(a) funcionário(a) {f2.getnome()} está alocado(a) no país: {f2.pais_alocacao()}")

print("_____________________________________________________________________________________")
print("Exercício 3: Qual o estado da filial que um funcionário coordena?")
filiais = [fil1, fil2]
encontrado = f3.estado_filial_coordenador(filiais)
if encontrado:
    print(f"O funcionário {f3.getnome()} coordena a filial no estado: {encontrado.getnome()}")
else:
    print(f"O funcionário {f3.getnome()} não coordena nenhuma filial")

encontrado = f1.estado_filial_coordenador(filiais)
if encontrado:
    print(f"O funcionário {f1.getnome()} coordena a filial no estado: {encontrado.getnome()}")
else:
    print(f"O funcionário {f1.getnome()} não coordena nenhuma filial")

print("_____________________________________________________________________________________")
print("Exercício 4: Qual a escolaridade do chefe de um departamento?")
print(f"A escolaridade do chefe do departamento {dep1.getnome()} é {dep1.escolaridade_chefe()}")

print("_____________________________________________________________________________________")
print("Exercício 5: Qual o nome do diretor da empresa de uma filial?")
print(f"O nome do(a) diretor(a) da empresa da filial {fil1.getnome()} é {fil1.nome_diretor_empresa()}")