from main import main


def test_main_quando_sucesso(capsys, definir_tabelas_saldos):
    """Teste as possíveis saídas do main.py para os casos de sucesso, conta de origem não existe, conta de destino não existe e saldo insuficiente

    Args:
        capsys (_type_): Para capturar a saída do print
        definir_tabelas_saldos (_type_): Fixture para definir os saldos das contas para teste
        transacao (_type_): Parametrized transaction data
    """
    transacao = [
        {
            # Sucesso
            "correlation_id": 1,
            "datetime": "01/09/2023 10:00:00",
            "conta_origem": 123,
            "conta_destino": 456,
            "valor": 100,
        }
    ]

    main(transacao)

    captured = capsys.readouterr()
    print(captured.out)
    assert "Origem  | antes: 500.00 -> depois: 400.00" in captured.out
    assert "Destino | antes: 0.00 -> depois: 100.00" in captured.out


def test_main_quando_nao_existe_conta_origem(capsys, definir_tabelas_saldos):
    transacao = [
        {
            # Falha - conta de origem não existe
            "correlation_id": 1,
            "datetime": "01/09/2023 10:00:00",
            "conta_origem": 000,
            "conta_destino": 456,
            "valor": 100,
        }
    ]

    main(transacao)

    captured = capsys.readouterr()
    print(captured.out)
    assert (
        "Transacao numero 1 foi cancelada. Conta de origem nao existe"
        in captured.out
    )


def test_main_quando_nao_existe_conta_destino(capsys, definir_tabelas_saldos):
    transacao = [
        {
            # Falha - conta de destino não existe
            "correlation_id": 1,
            "datetime": "01/09/2023 10:00:00",
            "conta_origem": 123,
            "conta_destino": 000,
            "valor": 100,
        }
    ]

    main(transacao)

    captured = capsys.readouterr()
    print(captured.out)
    assert (
        "Transacao numero 1 foi cancelada. Conta de destino nao existe"
        in captured.out
    )


def test_main_quando_saldo_insuficiente(capsys, definir_tabelas_saldos):
    transacao = [
        {
            # Falha - saldo insuficiente
            "correlation_id": 1,
            "datetime": "01/09/2023 10:00:00",
            "conta_origem": 123,
            "conta_destino": 456,
            "valor": 600,
        }
    ]

    main(transacao)

    captured = capsys.readouterr()
    print(captured.out)
    assert (
        "Transacao numero 1 foi cancelada. Saldo insuficiente" in captured.out
    )
