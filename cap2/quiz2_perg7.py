notas = (('Davi',  88,  95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))

_, _, math_scores, _ = zip(*notas)

media_matematica = sum(math_scores) / len(math_scores)

print(f"A média das notas de matemática é: {media_matematica}")