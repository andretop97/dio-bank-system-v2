from datetime import date
from classes.cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str) -> None:
        super().__init__(endereco, cpf)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento
