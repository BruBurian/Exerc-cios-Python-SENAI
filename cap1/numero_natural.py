def verifica_num_natural(num):
    if num >= 0:
        print(f"{num} é um numero natural")
        return True
    else: 
        print("")
        return False

num = int(input("Digite um numero entre -100 e 100: "))
resultado = verifica_num_natural(num)

print(resultado)