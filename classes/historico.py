from datetime import datetime

class Historico():
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self)-> list[dict]:
        return self._transacoes

    def adicionar_transacao(self, tipo: str, valor: float)-> None:
        self._transacoes.append({
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def gerar_relatorio(self, tipo = None):
        for transacao in self._transacoes:
            if not tipo:
                yield transacao

            if transacao['tipo'] == tipo:
                yield transacao
