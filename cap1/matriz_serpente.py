def matriz_serpente(n):
    matriz = [[0] * n for _ in range(n)]
    
    num = 1
    
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matriz[i][j] = num
                num += 1
        else:
            for j in range(n-1, -1, -1):
                matriz[i][j] = num
                num += 1
    
    for linha in matriz:
        print(' '.join(map(str, linha)))

n = int(input("Insira um número: "))
matriz_serpente(n)
