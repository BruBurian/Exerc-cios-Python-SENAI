print(50 * 2)
print('50' * 2)

str_number = '1' + '0' + '0' + '0'

number = int(str_number)

print(number) 

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

fatorial_5 = fatorial(5)
print(f"5! = {fatorial_5}")

# Calcular 10!
fatorial_10 = fatorial(10)
print(f"10! = {fatorial_10}")
