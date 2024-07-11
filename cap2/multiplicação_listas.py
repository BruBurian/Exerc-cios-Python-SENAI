# Declaração das listas
lista1 = [3, 5, 7]
lista2 = [2, 3, 4, 5, 6]

# Loop for aninhado para multiplicar cada elemento de lista1 por cada elemento de lista2
for i in lista1:
    for j in lista2:
        # Imprime o resultado da multiplicação
        print(f"{i} * {j} = {i * j}")