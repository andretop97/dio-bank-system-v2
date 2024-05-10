from classes.historico import Historico

class Conta:
    def __init__(self, numero: int, cliente_id: int) -> None:
        self._saldo: float = 0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: int = cliente_id
        self._historico: Historico = Historico()

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

    def depositar(self, valor: float) -> bool:
        if valor < 0:
            print("Operação negada. Valor tem que ser positivo")
            return False

        self._saldo += valor

        self.historico.adicionar_transacao("Deposito", valor)
        print(f"Deposito no valor de R$ {valor: .2f} realizado com sucesso")

        return True
