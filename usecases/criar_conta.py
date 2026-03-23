from domain.conta import Conta
from domain.cliente import Cliente

class CriarContaUseCase:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository

    def executar(self, numero, nome, cpf):
        cliente = Cliente(nome, cpf)
        conta = Conta(numero, cliente, 0)

        self.conta_repository.salvar(conta)