from controllers.acesso_dados import AcessoDados
from model.contas_saldos import ContaSaldo


def test_init(definir_tabelas_saldos):
    acesso_dados = AcessoDados()

    assert len(acesso_dados._TABELAS_SALDOS) == 2


def test__inicializar_saldos():
    acesso_dados = AcessoDados()

    assert len(acesso_dados._TABELAS_SALDOS) == 9


def test_get_saldo_quando_conta_existe(definir_tabelas_saldos):
    acesso_dados = AcessoDados()

    conta_saldo = acesso_dados.get_saldo(123)

    assert conta_saldo is not None
    assert conta_saldo.conta_id == 123
    assert conta_saldo.saldo == 500


def test_get_saldo_quando_conta_nao_existe(definir_tabelas_saldos):
    acesso_dados = AcessoDados()

    conta_saldo = acesso_dados.get_saldo(000)

    assert conta_saldo is None


def test_atualizar_conta_quando_conta_existe(definir_tabelas_saldos):
    acesso_dados = AcessoDados()

    conta_saldo_atualizada = acesso_dados.get_saldo(123)
    conta_saldo_atualizada.saldo = 300  # type: ignore

    resultado = acesso_dados.atualizar_conta(conta_saldo_atualizada)  # type: ignore

    assert resultado is True
    conta_saldo = acesso_dados.get_saldo(123)
    assert conta_saldo.saldo == 300  # type: ignore


def test_atualizar_conta_quando_conta_nao_existe(definir_tabelas_saldos):
    acesso_dados = AcessoDados()

    resultado = acesso_dados.atualizar_conta(
        ContaSaldo(conta_id=000, saldo=100)
    )

    assert resultado is False
