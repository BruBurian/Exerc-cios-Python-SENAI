def verificar_alfabeto(letra):
    letra = letra.lower()
    if letra in "aeiou":
        print(f"A letra {letra} É uma vogal")
    else:
        print(f"A letra {letra} É uma consoante")

letra = str(input("Digite uma letra: "))
resultado = (verificar_alfabeto(letra))

print(resultado)