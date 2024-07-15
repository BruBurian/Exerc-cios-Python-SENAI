a = [[1, 2], [3, 4], [5, 6]]

unidimensional = []

for sublist in a:
    for item in sublist:
        unidimensional.append(item)

print(unidimensional)