# Calculadora com operações básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

if __name__ == "__main__":
    print("Calculadora Básica")
    print("Soma: 2 + 3 =", soma(2, 3))
    print("Subtração: 5 - 2 =", subtracao(5, 2))
    print("Multiplicação: 3 * 4 =", multiplicacao(3, 4))
    print("Divisão: 10 / 2 =", divisao(10, 2))