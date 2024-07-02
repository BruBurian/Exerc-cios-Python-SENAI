# Funções para cada operação
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Divisão por zero não é permitida"
    return a / b

# Recebe o número da operação desejada
operacao = int(input("Digite o número da operação (1: Adição, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

# Recebe os dois números inteiros positivos
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Verifica a operação e imprime o resultado
if operacao == 1:
    resultado = adicionar(a, b)
    print("Resultado:", resultado)
elif operacao == 2:
    resultado = subtrair(a, b)
    print("Resultado:", resultado)
elif operacao == 3:
    resultado = multiplicar(a, b)
    print("Resultado:", resultado)
elif operacao == 4:
    resultado = dividir(a, b)
    print("Resultado:", resultado)
else:
    print("Inserido um número incorreto")