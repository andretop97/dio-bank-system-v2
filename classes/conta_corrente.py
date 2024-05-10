from datetime import datetime

from classes.conta import Conta
from classes.cliente import Cliente

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0, limite_saque: int = 3) -> None:
        super().__init__(numero, cliente)
        self._limite: float = limite
        self._limite_saques: int= limite_saque

        self.today: int = datetime.now().day
        self.daily_withdrawal_qtd = 0

    def sacar(self, valor: float) -> bool:
        if self.today != datetime.now().day:
            self.today = datetime.now().day
            self.daily_withdrawal_qtd = 0

        if self.daily_withdrawal_qtd >= self._limite_saques:
            print(f"Operação negada: Limite de {self._limite_saques} saques diario atingido")
            return False

        if valor > self._limite :
            print(f"Operação negada: Valor excede limite de R$ {self._limite: .2f}")
            return False

        if not super().sacar(valor):
            return False

        self.daily_withdrawal_qtd += 1

        return True
    