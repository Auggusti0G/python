"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema:

- Com base nos conceitos de Programação Orientada a Objetos (POO), vamos
trabalhar com duas classes (entidades).

- Implemente a entidade funcionário com estas características (atributos):
nome e salario.

- E implemente a entidade gerente com estas características (atributos):
nome, salario e quantidade de funcionários que ele gerencia.

-Implemente (Meet: vbc-shqr-wxd):

1- Implemente a classe Funcionario num arquivo separado do main.
2- Crie o método construtor (__init__), ele recebe os parâmetros que serão
   armazenados nos atributos da classe: nome e salário
class NomeClasse:
    def __init__ (self, parametro1, parametro2): # Sintaxe do construtor
        self.atributo1 = parametro1              # Atributos da classe
        self.atributo2 = parametro2

3- No método main, crie (instancie) dois objetos da classe e passe os argumentos
- Obs.: Implemente o main num segundo arquivo.py, separado das classes
# Sintaxe:
from nome_arquivo_sem_extensao import NomeClasse
if __name__ == '__main__':            # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2)  # Cria (instancia) o primeiro objeto da classe
4- No método main, mostre os objetos criados, teste (rode) a classe
   print("Objeto criado:", objeto1)              # Teste

5- Crie os métodos (defs) gets dos atributos para consultar os dados.
   def get_atributo1(self):           # Sintaxe do método get (consulta)
       return self.atributo1
6- No main, use (teste) os métodos gets para consultar os objetos criados
   print("Mensagem:", objeto1.get_atributo1()) # nome_objeto.nome_metodo()

7- Crie os métodos sets (defs) dos atributos para alterar os dados.
   def set_atributo1(self, novo_valor):  # sintaxe do método set (altera)
       self.atributo1 = novo_valor
8- No main, use (teste) os métodos sets para os alterar os objetos criados
   objeto1.set_atributo1(envia o novo valor). # nome_objeto.nome_metodo(novo_valor)
   print("Mensagem:", objeto1.get_atributo1()) # verifica se alterou na memória
---
9- Crie a classe Gerente, o construtor com os atributos nome, salario
   e quantidade de funcionários que ele gerencia.
10- No método main, crie (instancie) dois objetos da classe e passe os argumentos
11- Crie os métodos (defs) gets dos atributos para consultar os dados.
12- No main, use (teste) os métodos gets para consultar os objetos criados
13- Crie os métodos sets (defs) dos atributos para alterar os dados.
14- No main, use (teste) os métodos sets para os alterar os objetos criados
-----
Vamos usar os conceitos de herança (inheritance):
- Com base nos conceitos de Programação Orientada a Objetos (POO) e
    inheritance (herança), vamos usar duas ou mais classes (entidades).
- A classe funcionário com os atributos nome e salário é mais geral,
    então ela será a superclasse.
  E a classe gerente é mais específica com os atributos nome, salário e
    quantidade que gerencia, então ela será a subclasse.
  Ou seja, a subclasse Gerente herda da superclasse Funcionario
  - Sintaxe: class NomeSubclasse(NomeSuperclasse):
  - Exemplo: class Gerente(Funcionario):
1. Conceito de herança: eliminar código repetido, herdar os atributos repetidos
   Obs.: altere o construtor da subclasse Gerente.
   def __init__(self, nome, salario, qtd_gerencia):
       # self.nome = nome
       # self.salario = salario
       super().__init__(nome, salario)  # Chama o construtor da superclasse
       self.qtd_gerencia = qtd_gerencia
2. Conceito de herança: eliminar código repetido, herdar os métodos repetidos
   Obs.: Retire os métodos gets e sets repetidos da subclasse Gerente
         Não altere o main e rode com as alterações de herança realizadas.
-----
15- Todos os tipos de funcionário vão receber uma bonificação de 10% do valor
    do salário. Então, crie o método bonificacao, ele não recebe nada, calcula
    a bonificação e retorna o valor da bonificação
16- No main, Use o método bonificacao para as instâncias (objetos) f1 e g1.

"""

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Funcionario(object):
# class Funcionario():  # Três formas equivalentes de criar uma classe
class Funcionario:
    def __init__(self, nome, salario):  # Construtor
        self.nome = nome                # Atributos de instância
        self.salario = salario
    def get_nome(self):                 # Consulta e retorna pro main
        return self.nome
    def get_salario(self):
        return self.salario
    def set_nome(self, novo_nome):      # Altera o valor na memória
        self.nome = novo_nome
    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def bonificacao(self):
        bonus = self.salario * 0.10
        return bonus
    def mostra_dados(self):
        print("Nome: ", self.nome)
        print("Salário: ", self.salario)

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Gerente(object):
# class Gerente():      # Três formas equivalentes de criar a classe
class Gerente(Funcionario):
    def __init__(self, nome, salario, qtd_gerencia):  # Construtor
        # self.nome = nome                # Atributos de instância
        # self.salario = salario
        super().__init__(nome, salario)
        self.qtd_gerencia = qtd_gerencia
    # def get_nome(self):                 # Consulta e retorna pro main
    #     return self.nome
    # def get_salario(self):
    #     return self.salario
    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    # def set_nome(self, novo_nome):      # Altera o valor na memória
    #     self.nome = novo_nome
    # def set_salario(self, novo_salario):
    #     self.salario = novo_salario
    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd
