"""
1 - Primeiro passos no POO:
- Programação orientada a objetos é um paradigma de programação atualmente amplamente utilizada na criação de diversos projetos.

1° Criando os primeiros atributos
2° Criando o primeiro método
3° Passando parâmetros para os métodos
4° Diferença de chamar método e o atribúto
5° Passando a primeira def __init__ porém com parâmetros
"""

class TV:
    def __init__(self):
        self.cor = 'Preta'   #ATRIBUTO
        self.ligada = False  #ATRIBUTO
        self.tamanho = 55    #ATRIBUTO
        self.canal = 'Netflix'  #ATRIBUTO

    def mudar_cor(self): #CRIANDO O PRIMEIRO MÉTODO
        self.cor = 'Branca'

    def mudar_canal(self,novo_canal): #PASSANDO PARÂMETROS PARA NOSSOS MÉTODOS
        self.canal = novo_canal


tv_sala = TV()
tv_quarto = TV()

tv_quarto.mudar_cor()
print(tv_sala.cor)
print(tv_quarto.cor)

tv_quarto.mudar_canal('Globo') #USANDO MÉTODO:  ABRE-SE PARENTESES
print(tv_sala.canal) #DIFERENTE DE UM ATRIBUTO PASSA-SE:  APENAS ".ATRIBUTO_AQUI"
print(tv_quarto.canal)


class Playstation:
    def __init__(self,cor): # PODEMOS PASSAR OUTROS PARÂMETROS PARA A DEF __INIT__ COM ISSO O USUARIO PRECISARÁ FORNECER ESSE PARÂMETRO
        self.cor = cor
        self.ligada = False
        self.memoria = '4 GB'
        self.placa = 'GGTX4'

playstation_sala = Playstation('Preto') # Passando o parâmetro para a classe
print(playstation_sala.cor)


"""
2 - Criando o primeiro exemplo prático
"""
from datetime import datetime
import pytz
from random import randint
class ContaCorrente:
    #CRIANDO UM "DOCSTRING"
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): nome do cliente
        cpf (str): cpf do cliente
        agencia (int): agencia responsável pela conta do cliente
        conta (int): numero da conta do cliente
        saldo (int): saldo disponível para o cliente
        transcoes (list): histórico de transacoes do cliente
        limite (int): limite da conta do cliente

    """

    #MÉTODO ESTÁTICO: UM MÉTODO ESTÁTICA NÃO SE UTILIZA NENHUM PARÂMETRO DA CLASSE
    @staticmethod
    def _dataehora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
        pass

    def __init__(self,nome,cpf, agencia, conta): #__INIT__ MÉTODO CONSTRUTOR
        self._limite = None
        self._nome = nome #ATRIBUTOS QUE ESTÃO COM UM UNDERLINE _ NA FRENTE SÃO CONHECIDOS COMO ATRIBUTOS NÃO PÚBLICOS
        self._cpf = cpf    #ATRIBUTOS NÃO PÚBLICOS RESUMIDAMENTE SÃO ATRIBUTOS ÚNICOS QUE NÃO QUEREMOS ALTERAR FORA DA NOSSA CLASSE NO ENTANTO AINDA ASSIM PODE SER ACESSADO
        self._saldo = 0   #VIDE VER A LINHA 168 E 169
        self._agencia = agencia #ATRIBUTOS COM 2 UNDERLINE POSSUI A MESMA FUNCIONALIDADE DE 1 _ A DIFERENÇA É QUE ESSES NUNCA PODERÃO SER ACESSADOS DIFERENTE
        self._conta = conta
        self._transacoes = []
        self.cartões = []

    def consulta_saldo(self):
        # TAMBÉM É POSSÍVEL FAZER DOCSTRING PARA OS MÉTODOS
        """
            Exibe o saldo da conta do cliente
            não há parâmetros necessários
        :return:
        """
        print('seu saldo atual é de R${:,.2f}'.format(self._saldo))
        pass
    def depositar(self,valor):
        self._saldo += valor
        print('Deposito de R${:,.2f} realizado com sucesso'.format(valor))
        self._transacoes.append((valor, self._saldo, ContaCorrente._dataehora()))
        print(self.consulta_saldo())
        pass

    def _cheque_especial(self): # METODO AUXILIAR PARA SER UTILIZADO NO METODO SACAR_DINHEIRO
    # POR CONVERSÃO O UNDERLINE "_" É UTILIZADO PARA DESTACAR QUE ESSE MÉTODO É PRIVADO OU SEJA ELE É UM MÉTODO INTERNO DA CLASSE. OU SEJA DIFERENTE DO MÉTODO CONSULTA_SALDO
    # QUE NO QUAL PODE SER ACESSADO PELO USUÁRIO PARA VIZUALIZAR O SALDO. ESSE MÉTODO CHEQUE_ESPECIAL NÃO PODE SER ACESSADO PELO USUÁRIO OU SEJA NÃO POSSUI UTILIDADE PARA O USUARIO.
        self._limite = -1000
        return self._limite
        pass

    def consulta_cheque_especial(self):
        print('Seu limite de cheque especial é R${:,.2f}'.format(self._cheque_especial()))
        pass
    def sacar_dinheiro(self,valor):
        if self._saldo - valor < self._cheque_especial():
            print('Você não possui saldo suficiente')
            self.consulta_saldo()
        elif self._saldo - valor < 0:
            self._saldo -= valor
            print('Você entrou no cheque especial!')
            self.consulta_saldo()
        else:
            self._saldo -= valor
            print('Saque de R${:,.2f} realizado com sucesso'.format(valor))
            self._transacoes.append((-valor, self._saldo, ContaCorrente._dataehora()))
            print(self.consulta_saldo())
        pass

    def consulta_historico(self):
        print('Histórico de trancações:') # CRIANDO UM MÉTODO PARA CONSULTAR O HISTÓRICO DE TRANSAÇÕES
        for tracacao in self._transacoes:
            print(tracacao)
        pass

    def transferir(self,valor, conta_destino): #conta_destino é um objeto (instância) da nossa classe Conta_Corrente
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._dataehora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._dataehora()))
        print('Transferência realizada com sucesso!')
        pass

if __name__ == '__main__':
    #PROGRAMA COMEÇA AQUI
    Conta_Lucas = ContaCorrente('Lucas','182.969.677-74',0,223) # CRIADA A CONTA LUCAS
    Conta_Lucas.depositar(1000) # DEPOSITANDO DINHEIRO
    print('-'*100)
    Conta_Lucas.sacar_dinheiro(450) #SACANDO DINHEIRO
    print('-'*100)
    Conta_Lucas.sacar_dinheiro(800) # SACANDO MAIS DO QUE O SALDO E ENTRANDO EM CHEQUE ESPECIAL
    print('-'*100)
    Conta_Lucas.sacar_dinheiro(5000) # IMPEDINDO DE SACAR DEVIDO AO SALDO
    print('-'*100)
    Conta_Lucas.consulta_cheque_especial() # CONSULTANDO O LIMITE DO CHEQUE_ESPECIAL
    print('-'*100)
    Conta_Lucas.consulta_historico() #CONSULTANDO O HISTÓRICO DE TRANSAÇÕES
    print('-'*100)
    Conta_Lira = ContaCorrente('Lira','122.321.412-43',0,223) #CRIANDO UMA NOVA CONTA LIRA
    Conta_Lira.depositar(250) #DEPOSITANDO 250
    print('-'*100)
    Conta_Lira.transferir(250,Conta_Lucas) #TRANSFERINDO 250
    print('-'*100)
    Conta_Lira.consulta_saldo() #SALDO VOLTOU PARA O VALOR 0
    print('-'*100)
    Conta_Lucas.consulta_saldo() #SALDO VOLTOU PARA O VALOR 0
    print('-'*100)
    Conta_Lira.consulta_historico() #CONSULTANDO HISTORICO DA CONTA DO LIRA
    print('-'*100)
    help(ContaCorrente) # ACESSANDO O DOC STRING
    print('-'*100)
    print(Conta_Lucas._nome) # PRINTANDO O NOME COM 1 UNDERLINE _ PODE SER ACESSADO.
    print(Conta_Lucas._agencia) #TENTANDO PRINTA A AGENCIA COM 2 UNDERLINE NÃO PODERÁ ACESSAR
    print('-'*100)

class CartãoCredito:
    @staticmethod
    def _dataehora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self,titular,conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartãoCredito._dataehora().month, CartãoCredito._dataehora().year  + 5)
        self.codsegu = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartões.append(self)
        pass

    #ABAIXO METODO GET E SET
    @property  #PEGAR A INFORMAÇÃO DA SENHA
    def senha(self):
        return self._senha

    @senha.setter # VALIDAR A FORMA COM QUE SE MUDA O VALOR DA SENHA OU SEJA CRIA UMA REGRA
    def senha(self,valor):
        if len(valor) == 4 and valor.isnumeric():
                self._senha = valor
        else:
            print('Senha inválida')


if __name__ == '__main__':
    #PROGRAMA COMEÇA AQUI
    print('A PARTIR DAQUI OPERAÇÕES RELACIONADAS AO CARTÃO')
    print('-'*100)
    Cartão_Lucas = CartãoCredito('Lucas',Conta_Lucas)
    print(Cartão_Lucas.conta_corrente._conta) # PUXANDO A INFORMAÇÃO: A QUAL CONTA O CARTÃO DE CRÉDITO ESTÁ ASSOCIADO
    print('-'*100)
    print(Conta_Lucas.cartões) #PERCEBE-SE QUE EXISTE O OBJETO CARTÃO DENTRO DE UMA LISTA
    print('-'*100)
    print(Cartão_Lucas.numero) #IMPRIMINDO O NUMERO DO CARTÃO
    print('-'*100)

    print(Cartão_Lucas.codsegu) #IMRPIMINDO O COD DE SEGURANÇA DO CARTÃO
    print('-'*100)
    print(Cartão_Lucas.validade) #IMPRIMINDO A VALIDADE DO CARTÃO
    print('-'*100)
    Cartão_Lucas.senha = '12' #TENTANDO MUDAR A SENHA, IRÁ APARECER SENHA INVALIDA MOTIVO: VER LINHAS 193 A 202.
    print(Cartão_Lucas.senha) #ATENÇÃO PARA O .SENHA VEJA QUE NÃO É NECESSÁRIO POR O UNDERLINE _ POIS FOI O ATRIBUTO NO @PROPERTY COMO APENAS "SENHA"
    print('-'*100)
    print(Conta_Lucas.__dict__) ##__dict__ CONSULTA TODOS OS VALORES DE UMA INSTÂNCIA
    print(Conta_Lira.__dict__)

#FIM DO PROGRAMA
#OBSERVAÇÕES:
# 1° - if __name == '__main__' SERVE PARA NÃO EXISTIR CONFLITO NOS TESTES DOS ARQUIVOS DE CLASSE

