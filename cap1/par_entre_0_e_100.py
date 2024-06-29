num= int(input("Digite um numero: "))

if 0<= num <= 100:
    if num % 2 == 0:
        print(f"O numero {num} é um numero par entre 0 e 100")
    else:
        print(f"O numero {num} não é par")
else:
    print(f"O número {num} não está entre 0 e 100")