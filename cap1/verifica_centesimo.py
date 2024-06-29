def verifica_centesimo(num):
    if num <100 or num > 999:
        return False

    centesimo = (num // 100)

    if centesimo != 3:
        return False
    else:
        return True
    
num = int(input("digite um numero de 3 digitos: "))
resultado = verifica_centesimo(num)

print(resultado)