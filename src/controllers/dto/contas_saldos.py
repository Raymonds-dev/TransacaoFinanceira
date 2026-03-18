class ContaSaldo():
    def __init__(self, conta: int, saldo: float) -> None:
        self.conta = conta
        self.saldo = saldo

    def get_conta(self):
        return self.conta

    def set_conta(self, value):
        self.conta = value

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, value):
        self.saldo = value
