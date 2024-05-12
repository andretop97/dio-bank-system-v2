import uuid
from classes.conta import Conta

class Cliente():
    def __init__(self, endereco: str, identificador: str) -> None:
        self._endereco: str = endereco
        self._contas: list[Conta] = []
        self._id: uuid.UUID = uuid.uuid4()
        self._identificador: str = identificador
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: ({self._identificador})>'

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def identificador(self) -> str:
        return self._identificador

    def adicionar_conta(self, conta: Conta) -> None:
        self._contas.append(conta)
