# ⚡ Exercício Relâmpago Surpresa

As linhas do diagrama representam **associações entre classes**.  
As **setas** indicam o **sentido da comunicação**.  
O número **"1"** indica que apenas um objeto está relacionado.  
Você deverá escolher se cada associação será **obrigatória** ou **opcional**.

---

## 📘 Diagrama

<img width="364" height="306" alt="image" src="https://github.com/user-attachments/assets/ab7f4f93-21dc-44ea-af26-876b8867845f" />


O diagrama de classes mostra as seguintes entidades:

- **Grupo**
- **País**
- **Empresa**
- **Estado**
- **Cidade**
- **Filial**
- **Departamento**
- **Funcionário**
- **Escolaridade**

As relações principais incluem:
- Grupo possui um presidente.
- Empresa possui um diretor e está associada a um grupo.
- Funcionário possui escolaridade e coordena um departamento.
- Filial pertence a uma empresa e está localizada em uma cidade.
- Cada cidade pertence a um estado e a um país.

---

## 🧩 Desafio

Com base no diagrama acima, escreva código que responda às seguintes questões:

1. Qual a **escolaridade do presidente de um grupo**?
2. Qual o **país de alocação de um funcionário**?
3. Qual o **estado da filial** que um funcionário coordena?
4. Qual a **escolaridade do chefe de um departamento**?
5. Qual o **nome do diretor da empresa de uma filial**?

---

## 💡 Dica

Utilize os métodos `get` e as associações entre as classes para navegar nas relações.  
Pense em como os objetos se conectam para chegar às respostas.

---

## 📎 Exemplo de Estrutura de Classes (sugestão)

```python
class Grupo:
    def __init__(self, presidente):
        self.__presidente = presidente

    def get_presidente(self):
        return self.__presidente


class Funcionario:
    def __init__(self, nome, escolaridade):
        self.__nome = nome
        self.__escolaridade = escolaridade

    def get_escolaridade(self):
        return self.__escolaridade


class Empresa:
    def __init__(self, diretor, grupo):
        self.__diretor = diretor
        self.__grupo = grupo

    def get_diretor(self):
        return self.__diretor

    def get_grupo(self):
        return self.__grupo
```

---

## ✍️ Tarefa

Implemente as classes e escreva um **programa principal (main.py)** que:
- Crie os objetos conforme o diagrama;
- Estabeleça as relações entre eles;
- Imprima as respostas para as 5 perguntas.

---

## 🚀 Objetivo

Este exercício serve para **treinar o raciocínio sobre associações entre classes** e a **navegação entre objetos** em Programação Orientada a Objetos.
