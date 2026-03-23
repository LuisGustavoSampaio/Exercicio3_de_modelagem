class RealizarSaqueUseCase:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository

    def executar(self, numero_conta, valor):
        conta = self.conta_repository.buscar(numero_conta)

        if conta:
            sucesso = conta.sacar(valor)
            if sucesso:
                self.conta_repository.salvar(conta)
            else:
                print("Saldo insuficiente")