class Conta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f"Deposito: {valor}")

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        self.historico.append(f"Saque: {valor}")
        return True