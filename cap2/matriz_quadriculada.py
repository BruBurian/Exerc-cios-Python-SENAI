def criar_matriz_quadriculada(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if (i + j) % 2 == 0:
                linha.append('1')
            else:
                linha.append('0')
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(' '.join(linha))

# Solicita ao usuário o valor de n
n = int(input("Informe n: "))

# Verifica se n é maior ou igual a 2
if n >= 2:
    matriz = criar_matriz_quadriculada(n)
    imprimir_matriz(matriz)
else:
    print("O valor de n deve ser maior ou igual a 2.")