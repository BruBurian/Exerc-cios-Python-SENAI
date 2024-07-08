numero = 1

while numero <= 9:
    contador = 1
    while contador <= 10:
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")
        contador += 1
    print()
    numero += 1