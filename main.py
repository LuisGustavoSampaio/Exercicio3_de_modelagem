from infraestrutura.arquivo_conta_repositorio import ArquivoContaRepository
from usecases.criar_conta import CriarContaUseCase
from usecases.depositar import DepositarUseCase
from usecases.sacar import RealizarSaqueUseCase

repo = ArquivoContaRepository()

criar_conta = CriarContaUseCase(repo)
depositar = DepositarUseCase(repo)
sacar = RealizarSaqueUseCase(repo)

criar_conta.executar(1, "Gustavo", "123")
depositar.executar(1, 100)
sacar.executar(1, 50)