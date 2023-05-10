#Defininfo classe
class ContaBancaria:
    
    def __init__(self, nome_do_titular, saldo_inicial):
        self.nome_do_titular = nome_do_titular
        self.saldo = saldo_inicial

    def exibir_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo}')

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print(f'Valor de R$ {valor_deposito} foi depositado na sua conta')

    def sacar(self, valor_saque):
        self.saldo -= valor_saque
        print(f'Valor de R$ {valor_saque} foi debitado da sua conta')


conta1 = ContaBancaria('José',300)
conta1.depositar(50)
