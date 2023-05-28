from IntroduçãoaPOO import ContaCorrente,CartãoCredito
from Agencias import Agencia,AgenciaComum,AgenciaVirtual,AgenciaPremium

#PROGRAMA PARA MANIPULAÇÃO DA CONTA CORRENTE
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


#PROGRAMA PARA MANIPULAÇÃO DO CARTÃO DO CLIENTE
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

#PROGRAMA PARA MANIPULAÇÃO AGENCIAS
agencia1 = Agencia(2187658934, 1276684789, 2456)
agencia1.verifica_caixa()  # CAIXA ABAIXO DO RECOMENDO

agenciavirtual = AgenciaVirtual('www.agenciavirtual.com', 12332231, 312312312)
agenciavirtual.verifica_caixa()  # AGENCIA VIRTUAL CAIXA EM NÍVEL ESTÁVEL

agenciacomum = AgenciaComum(232323, 3232332)
agenciacomum.verifica_caixa()  # AGENCIA COMUM CAIXA EM NÍVEL ESTÁVEL

agenciapremium = AgenciaPremium(212332, 4322343)
agenciapremium.verifica_caixa()  # AGENCIA PREMIUM CAIXA EM NÍVEL ESTÁVEL
print('-' * 100)
agenciavirtual.depositar_paypal(50000)
print(agenciavirtual.caixa)
print(agenciavirtual.caixa_paypal)
agenciavirtual.verifica_caixa()
print('-' * 100)
agenciapremium.adicionar_cliente('Lucas', 18296967774, 10000)  # CLIENTE NÃO ELEGÍVEL PARA A CONTA PREMIUM
