from datetime import datetime

def log(function: callable)-> None:
    def envelope(*args, **kwargs):
        resultado = function(*args,**kwargs)
        print(f'Função: {function.__name__}, horario de execução: {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')
        return resultado

    return envelope
