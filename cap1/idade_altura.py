def roler_coaster(idade, altura):
    print("Super Montanha Russa")
    if idade >= 16 and altura >= 150:
        print("Você pode entrar")
    else:
        print("Você não pode entrar")

idade = int(input("Digite sua idade: "))
altura = int(input("Digite sua altura: "))

resultado = roler_coaster(idade, altura)
print(resultado)
    