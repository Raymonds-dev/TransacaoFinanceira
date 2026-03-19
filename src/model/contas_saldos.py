class ContaSaldo:
    """Representa uma conta bancária"""

    def __init__(self, conta_id: int, saldo: float) -> None:
        self.conta_id = conta_id
        self.saldo = saldo
