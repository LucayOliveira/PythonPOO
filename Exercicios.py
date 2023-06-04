"""
NÍVEL 1 FÁCIL (COMPLETO):

Exercício 1:
Crie uma classe chamada "Cachorro" com um método chamado "latir". O método "latir" deve exibir a mensagem "Au au!".

Exercício 2:
Crie uma classe chamada "Carro" com os atributos "marca" e "modelo". Em seguida, crie um objeto dessa classe e exiba a marca e o modelo do carro.

Exercício 3:
Crie uma classe chamada "Retangulo" com os atributos "largura" e "altura". Em seguida, crie um método chamado "calcular_area" que calcula e retorna a área do retângulo.

Exercício 4:
Crie uma classe chamada "ContaBancaria" com os atributos "titular" e "saldo". Em seguida, crie os métodos "depositar" e "sacar" que permitem adicionar e retirar dinheiro da conta.

Exercício 5:
Crie uma classe chamada "Aluno" com os atributos "nome" e "nota". Em seguida, crie um método chamado "verificar_aprovacao" que verifica se o aluno foi aprovado (nota maior ou igual a 7) ou reprovado (nota menor que 7).


#Resolução Exercício 1:
class Cachorro:
    @staticmethod
    def latir():
        return print('Au Au!')
    pass
Cachorro.latir()

# Resolução Exercício 2:
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro = Carro('Volkswagen','Fusca')
print(carro.marca)
print(carro.modelo)

# Resolução Exercício 3:
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcula_area(self):
        calculo =  self.largura * self.altura
        return print('Área: {} metros quadrados'.format(calculo))

Valores = Retangulo(10,20)
Valores.calcula_area()

# Resolução Exercício 4:
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return print('Depósito realizado com sucesso! Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))
        pass

    def sacar(self, valor):
        self.saldo -= valor
        return print('Saque relizado com sucesso! Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

Conta = ContaBancaria('Lucas',200)
Conta.depositar(100)
Conta.sacar(50)

# Resolução Exercício 5:

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 7:
            return print('Aluno Aprovado')
        else:
            return print('Aluno reprovado')

Aluno1 = Aluno('Lucas', 7.5)
Aluno2 = Aluno('Matheus', 4)
Aluno1.verificar_aprovacao()
Aluno2.verificar_aprovacao()
"""






