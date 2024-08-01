def potencia_recursiva(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia_recursiva(x, n - 1)
a
x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

resultado = potencia_recursiva(x, n)

print(f"{x} elevado a {n} é: {resultado}")