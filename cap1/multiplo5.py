def multiplo_5(num):
    if num % 5 == 0:
        return True
    else: 
        return False
    
num = int(input("Digite um numero: "))
resultado = multiplo_5(num)

print(resultado)