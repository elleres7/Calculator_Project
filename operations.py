# Atualizando as funções para retornarem valores ao invés de imprimir

def som(x, y):
    return x + y  # Agora retorna o valor ao invés de imprimir

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Não se pode dividir por Zero!")  # Levanta uma exceção para zero
    return x / y  # Retorna o resultado da divisão