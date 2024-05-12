from datetime import datetime
from functools import wraps

from classes.conta import Conta
from classes.cliente import Cliente
from utils.decorators import log

class ContaCorrente(Conta):
    def _validar_limite_transacao(func: callable):
        @wraps(func)
        def envelope(self, *args, **kwargs):
            if self._hoje != datetime.now().date():
                self._hoje = datetime.now().date()
                self._qtd_transacao_diaria = 0
                self._daily_withdrawal_qtd = 0

            if self._qtd_transacao_diaria >= self._limite_transacao_diaria:
                print("Operacao negada: Limite de transações diarias atingido")
                return

            resultado = func(self, *args, **kwargs)

            self._qtd_transacao_diaria += 1

            return resultado

        return envelope
    
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0, limite_saque: int = 3) -> None:
        super().__init__(numero, cliente)
        self._limite: float = limite
        self._limite_saques: int= limite_saque

        self._daily_withdrawal_qtd = 0

    @log
    @_validar_limite_transacao
    def sacar(self, valor: float) -> bool:
        if self._daily_withdrawal_qtd >= self._limite_saques:
            print(f"Operação negada: Limite de {self._limite_saques} saques diario atingido")
            return False

        if valor > self._limite :
            print(f"Operação negada: Valor excede limite de R$ {self._limite: .2f}")
            return False

        if not super().sacar(valor):
            return False

        self._daily_withdrawal_qtd += 1

        return True
    