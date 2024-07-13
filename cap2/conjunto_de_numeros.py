minha_lista = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

a, b = map(int, input("Digite dois números inteiros: ").split())

if (a, b) in minha_lista:
    posicao = minha_lista.index((a, b))
    print(f'Há ({a},{b}) na posição {posicao}.')
elif (b, a) in minha_lista:
    posicao = minha_lista.index((b, a))
    print(f'Não há ({a},{b}), mas há ({b},{a}) na posição {posicao}.')
else:
    print(f'não há ({a},{b}) nem ({b},{a}).')