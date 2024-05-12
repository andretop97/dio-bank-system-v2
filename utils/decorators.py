from datetime import datetime

def log(function: callable)-> None:
    def envelope(*args, **kwargs):
        resultado = function(*args,**kwargs)
        try:
            with open("log.txt", "a") as log:
                log.write(f'{{funcao: {function.__name__.upper()},  args: {args}, kwargs: {kwargs}, resultado: {resultado}, data: {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}}}\n')
                return resultado
        except Exception as err:
            print(f"Operação falho: Erro interno do sistema {err}")

    return envelope
