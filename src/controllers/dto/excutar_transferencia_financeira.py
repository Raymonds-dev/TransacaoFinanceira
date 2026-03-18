from contas_saldos import ContaSaldo
from acesso_dados import AcessoDados


class ExecutarTransferenciaFinanceira(AcessoDados):
    def transferir(
        self,
        correlation_id: int,
        conta_origem: int,
        conta_destino: int,
        valor: float,
    ) -> None:

        conta_saldo_origem = ContaSaldo(conta_origem, valor)
        conta_saldo_destino = ContaSaldo(conta_destino, valor)
