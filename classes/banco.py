from datetime import datetime

from classes.cliente import Cliente
from classes.conta import Conta

from utils.decorators import log
from utils.list_operations import find_object_by_attribute


class Bank:
    def __init__(self) -> None:
        self._contas: list[Conta] = []
        self._clientes: list[Cliente] = []
        self._count = 0

    @log
    def criar_conta(self, identificador: str) -> None:
        self._count += 1

        cliente: Cliente = self.get_cliente(identificador)
        if not cliente:
            print("Operação negada: Não foi encontrado cliente com esse cpf")
            return
        nova_conta = Conta(self._count, cliente)
        cliente.adicionar_conta(nova_conta)
        self._contas.append(nova_conta)
        print("Conta cadastrada com sucesso")

    @log
    def criar_cliente(self, endereco: str, identificador: str) -> None:
        user = find_object_by_attribute(self._clientes, "identificador", identificador)
        if user:
            print("Operação negada: Identificador informado ja registrado")
            return

        novo_cliente = Cliente(endereco, identificador)
        self._clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso")

    @log
    def listar_contas(self, identificador: str) -> list[Conta]:
        cliente: Cliente = find_object_by_attribute(self._clientes, "identificador", identificador)
        if not cliente:
            print("Operação negada: identificador informado não tem contas cadastrado")
            return []
        
        return [account for account in self._contas if account.cliente.id == cliente.id]

    def get_conta(self, account_number: int) -> Conta:
        return find_object_by_attribute(self._contas, "numero", account_number)

    def get_cliente(self, identificador: str) -> Cliente:
        return find_object_by_attribute(self._clientes, "identificador", identificador)

    def menu_principal(self) -> int:
        menu: str = '''
Digite um dos valores a baixo para realizar uma operação:
    [1] Criar cliente
    [2] Criar conta
    [3] Listar contas para usuario
    [4] Operações da conta
    [5] Finalizar operação
    =>  '''

        command = int(input(menu))

        if command == 1:
            identificador = input("Informe seu CPF: ")
            endereco = input("Informe seu endereço: ")
            self.criar_cliente(endereco, identificador)
            return -1

        elif command == 2:
            identificador = input("Informe seu cpf: ")
            self.criar_conta(identificador)

            return -1
        elif command == 3:
            identificador = input("Informe seu cpf: ")
            contas = self.listar_contas(identificador)
            
            for conta in contas:
                print(f"[{conta.numero}]: agencia {conta.agencia} , numero {conta.numero} ")

            return -1
        elif command == 4:
            identificador = input("Informe seu cpf: ")
            contas = self.listar_contas(identificador)

            if not contas:
                return -1

            print("Escolha uma conta :")
            valid_input = []
            for conta in contas:
                valid_input.append(conta.numero)
                print(f"[{conta.numero}]: agencia {conta.agencia} , numero {conta.numero} ")
            numero = int(input("=>"))

            if numero not in valid_input:
                print("Operação negada: opção selecionada não corresponde a uma de suas contas")
                return -1
            return numero

        elif command == 5:
            return None
        else:
            print("Comando invalido, por favor tente novamente")
            return -1

    def menu_conta(self, numero: int) -> int:
        menu: str = '''
Digite um dos valores a baixo para realizar uma operação:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => '''
        conta: Conta = self.get_conta(numero)
        command = str(input(menu))

        if command == "d":
            valor = float(input("Informe o valor do deposito: "))
            conta.depositar(valor)
            return numero
        elif command == "s":
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor=valor)
            return numero
        elif command == "e":
            transacoes = conta.historico.gerar_relatorio()
            for transacao in transacoes:
                print(f'Tipo: {transacao["tipo"]}, valor: {transacao["valor"]}, data: {transacao["data"]}.')
            print(f'\nSaldo: R$ {conta.saldo: .2f}')

            return numero
        elif command == 'q':
            return -1
        else:
            print("Comando invalido, por favor tente novamente")
            return numero
