from classes.banco import Bank

if __name__ == '__main__':
    banco = Bank()

    numero: int = -1
    while True:
        if numero == None:
            break
        elif numero > 0:
            numero = banco.menu_conta(numero)
        else:
            numero = banco.menu_principal()
