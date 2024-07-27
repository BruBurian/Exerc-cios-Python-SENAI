def verifica_multiplo(a, b):a
    if a % b == 0:
        print(f"{a} é multiplo de {b}")
    else:
        print(f"{a} não é multiplo de {b}")

a = int(input("insira um valor para ser o A: "))
b = int(input("insira um valor para ser o B: "))

resultado = verifica_multiplo(a, b)

print(resultado)
