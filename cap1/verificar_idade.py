def verifica_idade(idade):
    if idade >= 20:
        print("Você é adulto")
        return True
    elif idade > 10:
        print("Você é jovem")
        return True
    else:
        print("Você é criança")
        return True

idade = int(input("Digite sua idade: "))
resultado = verifica_idade(idade)

print(resultado)