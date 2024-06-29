print("Ano bissexto")
ano = int(input("Insira o ano: "))
calculo = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
print(calculo) 
