lista = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']

lista_sem_vazios = []

for elemento in lista:
    if isinstance(elemento, tuple) and len(elemento) == 0:
        lista_sem_vazios.append(elemento)
    elif isinstance(elemento, (str, list, tuple)) and len(elemento) == 0:
        continue
    else:
        lista_sem_vazios.append(elemento)

print("a lista sem os elementos vazios:", lista_sem_vazios)
