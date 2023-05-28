class Agencia:
    def __init__(self,telefone, cnpj, numero):
        self.telefone = telefone
        self.numero = numero
        self.cnpj = cnpj
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verifica_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual R$ {:,.2f}'.format(self.caixa))
        else:
            print('Caixa em nível recomendado. Caixa atual R$ {:,.2f}'.format(self.caixa))
        pass

    def emprestar_dinheiro(self,valor,cpf,juros):
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf,juros))
        else:
            print('Empréstimo dinheiro dinheiro em caixa insuficiente')
        pass

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome,cpf,patrimonio))
        pass

#CRIANDO 3 SUBCLASSES:
#AGENCIA VIRTUAL
#AGENCIA COMUM
#AGENCIA PREMIUM
#TODAS AS 3 CLASSES NOVAS CRIADAS TERÃO HERANÇAS OU SEJA ELAS HERDÃO A HERANÇA QUE NO CASO SERIAM INFORMAÇÕES DA CLASSE PRINCIPAL

from random import randint

class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj ):
        self.site = site
        super().__init__(telefone,cnpj,1000) #CHAMANDO O METODO INIT DA AGENCIA PRINCIPAL
        self.caixa = 1000000
        self.caixa_paypal = 0
    pass

    def depositar_paypal(self, valor):
        self.caixa -=valor
        self.caixa_paypal += valor
        pass

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        pass

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1000, 9999))
        self.caixa = 1000000
    pass

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1000, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio) #POLIMORFISMO PEGAR METODO E APLICA-LO DE FORMA DIFERENTE EM CLASSES DIFERENTE
        else:
            print('Cliente não é elegível para a conta premium')
    pass

if __name__ == '__main__':
    agencia1 = Agencia(2187658934,1276684789,2456)
    agencia1.verifica_caixa() # CAIXA ABAIXO DO RECOMENDO

    agenciavirtual = AgenciaVirtual('www.agenciavirtual.com',12332231,312312312)
    agenciavirtual.verifica_caixa() #AGENCIA VIRTUAL CAIXA EM NÍVEL ESTÁVEL

    agenciacomum = AgenciaComum(232323,3232332)
    agenciacomum.verifica_caixa() #AGENCIA COMUM CAIXA EM NÍVEL ESTÁVEL

    agenciapremium = AgenciaPremium(212332,4322343)
    agenciapremium.verifica_caixa() #AGENCIA PREMIUM CAIXA EM NÍVEL ESTÁVEL
    print('-'*100)
    agenciavirtual.depositar_paypal(50000)
    print(agenciavirtual.caixa)
    print(agenciavirtual.caixa_paypal)
    agenciavirtual.verifica_caixa()
    print('-'*100)
    agenciapremium.adicionar_cliente('Lucas',18296967774,10000) #CLIENTE NÃO ELEGÍVEL PARA A CONTA PREMIUM


#FIM DO PROGRAMA
#OBSERVAÇÕES:
# 1° - if __name == '__main__' SERVE PARA NÃO EXISTIR CONFLITO NOS TESTES DOS ARQUIVOS DE CLASSE
# 2° -





