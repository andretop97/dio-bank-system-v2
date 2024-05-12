from classes.conta import Conta

class ContaIterador:
    def __init__(self, contas: list[Conta]) -> None:
        self._contas : list[Conta] = contas
        self._index: int = 0 

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self._contas[self._index]
            return { "Numero": conta.numero, "Agencia": conta.agencia, "Saldo": conta.saldo}
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1
        
