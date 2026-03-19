# src/tests/conftest.py
import pytest
from controllers.acesso_dados import AcessoDados
from model.contas_saldos import ContaSaldo


@pytest.fixture
def definir_tabelas_saldos(monkeypatch):
    def _inicializar_saldos_teste(self):
        self._TABELAS_SALDOS = [
            ContaSaldo(conta_id=123, saldo=500),
            ContaSaldo(conta_id=456, saldo=0),
        ]

    monkeypatch.setattr(
        AcessoDados, "_inicializar_saldos", _inicializar_saldos_teste
    )
