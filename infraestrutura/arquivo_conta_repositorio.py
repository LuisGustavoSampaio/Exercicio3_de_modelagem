from interfaces.iconta_repository import IContaRepository
from domain.conta import Conta
from domain.cliente import Cliente

class ArquivoContaRepository(IContaRepository):

    def __init__(self, arquivo="contas.txt"):
        self.arquivo = arquivo

    def salvar(self, conta):
        with open(self.arquivo, "a") as f:
            f.write(f"{conta.numero},{conta.cliente.nome},{conta.saldo}\n")

    def buscar(self, numero):
        try:
            with open(self.arquivo, "r") as f:
                for linha in f:
                    dados = linha.strip().split(",")
                    if int(dados[0]) == numero:
                        cliente = Cliente(dados[1], "")
                        return Conta(numero, cliente, float(dados[2]))
        except FileNotFoundError:
            return None