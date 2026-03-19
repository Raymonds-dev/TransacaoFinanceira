from controllers.acesso_dados import AcessoDados
import threading


lock = threading.Lock()


class ExecutarTransferenciaFinanceira(AcessoDados):
    """Executa transferências financeiras entre contas

    Args:
        AcessoDados (AcessoDados): Gerencia o acesso aos dados de uma conta
    """

    def transferir(
        self,
        correlation_id: int,
        conta_origem: int,
        conta_destino: int,
        valor: float,
    ) -> None:

        conta_saldo_origem = self.get_saldo(conta_origem)
        conta_saldo_destino = self.get_saldo(conta_destino)

        if not conta_saldo_origem:
            print(
                "\n" + "=" * 58 + "\n"
                f"Transacao numero {correlation_id} foi cancelada. Conta de origem nao existe\n"
                + "="
                * 58
            )
            return
        if not conta_saldo_destino:
            print(
                "\n" + "=" * 58 + "\n"
                f"Transacao numero {correlation_id} foi cancelada. Conta de destino nao existe\n"
                + "="
                * 58
            )
            return

        if conta_saldo_origem.saldo < valor:
            print(
                "\n" + "=" * 58 + "\n"
                f"Transacao numero {correlation_id} foi cancelada. Saldo insuficiente\n"
                + "="
                * 58
            )
            return

        with lock:
            saldo_origem_antes = conta_saldo_origem.saldo
            saldo_destino_antes = conta_saldo_destino.saldo

            conta_saldo_origem.saldo -= valor
            conta_saldo_destino.saldo += valor

            saldo_origem_depois = conta_saldo_origem.saldo
            saldo_destino_depois = conta_saldo_destino.saldo

        print(
            "\n" + "=" * 58 + "\n"
            f" TRANSACAO #{correlation_id} - SUCESSO\n" + "-" * 58 + "\n"
            f" Conta origem   : {conta_origem}\n"
            f" Conta destino  : {conta_destino}\n"
            f" Valor transfer.: {valor:.2f}\n" + "-" * 58 + "\n"
            f" Origem  | antes: {saldo_origem_antes:.2f} -> depois: {saldo_origem_depois:.2f}\n"
            f" Destino | antes: {saldo_destino_antes:.2f} -> depois: {saldo_destino_depois:.2f}\n"
            + "="
            * 58
        )
