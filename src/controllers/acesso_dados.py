from model.contas_saldos import ContaSaldo


class AcessoDados:
    """Gerencia o acesso aos dados de contas e saldos"""

    def __init__(self) -> None:
        self._TABELAS_SALDOS: list[ContaSaldo] = []
        self._inicializar_saldos()

    def _inicializar_saldos(self):
        """Inicializa a classe com contas padrão e valores padrões"""
        self._TABELAS_SALDOS.append(ContaSaldo(938485762, 180))
        self._TABELAS_SALDOS.append(ContaSaldo(347586970, 1200))
        self._TABELAS_SALDOS.append(ContaSaldo(2147483649, 0))
        self._TABELAS_SALDOS.append(ContaSaldo(675869708, 4900))
        self._TABELAS_SALDOS.append(ContaSaldo(238596054, 478))
        self._TABELAS_SALDOS.append(ContaSaldo(573659065, 787))
        self._TABELAS_SALDOS.append(ContaSaldo(210385733, 10))
        self._TABELAS_SALDOS.append(ContaSaldo(674038564, 400))
        self._TABELAS_SALDOS.append(ContaSaldo(563856300, 1200))

    def get_saldo(self, conta_id: int) -> ContaSaldo | None:
        """Consulta o saldo de uma conta

        Args:
            conta_id (int): ID da conta que atualizará o saldo

        Returns:
            ContaSaldo | None: Retorna o objeto ContaSaldo ou None caso não encontre a conta informada
        """
        return next(
            (
                conta
                for conta in self._TABELAS_SALDOS
                if conta.conta_id == conta_id
            ),
            None,
        )

    def atualizar_conta(self, conta_atualizada: ContaSaldo) -> bool:
        """Atualiza o saldo de uma conta

        Args:
            conta_atualizada (ContaSaldo): Conta a ser atualizada

        Returns:
            bool: True se atualizada e False caso erro ou conta não encontrada
        """
        conta_existente = self.get_saldo(conta_atualizada.conta_id)
        if conta_existente is None:
            return False

        self._TABELAS_SALDOS = [
            conta
            for conta in self._TABELAS_SALDOS
            if conta.conta_id != conta_atualizada.conta_id
        ]

        self._TABELAS_SALDOS.append(conta_atualizada)
        return True
