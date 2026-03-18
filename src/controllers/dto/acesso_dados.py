from contas_saldos import ContaSaldo


class AcessoDados:
    def __init__(self) -> None:
        self._TABELAS_SALDOS: list[ContaSaldo] = []
        self._inicializar_saldos()

    def _inicializar_saldos(self):
        self._TABELAS_SALDOS.append(ContaSaldo(938485762, 180))
        self._TABELAS_SALDOS.append(ContaSaldo(347586970, 1200))
        self._TABELAS_SALDOS.append(ContaSaldo(2147483649, 0))
        self._TABELAS_SALDOS.append(ContaSaldo(675869708, 4900))
        self._TABELAS_SALDOS.append(ContaSaldo(238596054, 478))
        self._TABELAS_SALDOS.append(ContaSaldo(573659065, 787))
        self._TABELAS_SALDOS.append(ContaSaldo(210385733, 10))
        self._TABELAS_SALDOS.append(ContaSaldo(674038564, 400))
        self._TABELAS_SALDOS.append(ContaSaldo(563856300, 1200))
