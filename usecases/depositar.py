class DepositarUseCase:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository

    def executar(self, numero_conta, valor):
        conta = self.conta_repository.buscar(numero_conta)

        if conta:
            conta.depositar(valor)
            self.conta_repository.salvar(conta)