from datetime import datetime, date
from functools import wraps

from classes.historico import Historico
from utils.decorators import log

class Conta:
    def _validar_limite_transacao(func: callable):
        @wraps(func)
        def envelope(self, *args, **kwargs):
            if self._hoje != datetime.now().date():
                self._hoje = datetime.now().date()
                self._qtd_transacao_diaria = 0
                print("Batata")

            if self._qtd_transacao_diaria >= self._limite_transacao_diaria:
                print("Operacao negada: Limite de transações diarias atingido")
                return

            resultado = func(self, *args, **kwargs)

            self._qtd_transacao_diaria += 1

            return resultado

        return envelope
    
    def __init__(self, numero: int, cliente_id: int, limite_transacao_diaria: int = 3) -> None:
        self._saldo: float = 0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: int = cliente_id
        self._historico: Historico = Historico()

        self._limite_transacao_diaria = limite_transacao_diaria
        self._qtd_transacao_diaria = 0
        self._hoje: date = datetime.now().date()

    def __str__(self) -> str:
        return f'{{conta: {self._numero}, agencia: {self._agencia}, cliente: {self._cliente}}}'
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: ({self.numero})>'
    
    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> int:
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico


    @classmethod
    def nova_conta(cls, cliente_id: int, numero: int):
        return cls(numero, cliente_id)

    @log
    @_validar_limite_transacao
    def sacar(self, valor: float) -> bool:
        if valor > self._saldo:
            print("Operação negada: Valor requerido superior ao seu saldo")
            return False

        if valor < 0 :
            print("Operação negada: Valido somente valores positivos")
            return False

        self._saldo -= valor
        self.historico.adicionar_transacao("Saque", valor)

        print(f"Saque no valor de R$ {valor: .2f} realizado com sucesso")

        return True

    @log
    @_validar_limite_transacao
    def depositar(self, valor: float) -> bool:
        if valor < 0:
            print("Operação negada. Valor tem que ser positivo")
            return False

        self._saldo += valor

        self.historico.adicionar_transacao("Deposito", valor)
        print(f"Deposito no valor de R$ {valor: .2f} realizado com sucesso")

        return True
