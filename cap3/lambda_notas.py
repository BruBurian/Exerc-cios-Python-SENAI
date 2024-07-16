notas = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

tamanho_conjunto = 3

sublistas_notas = [notas[i:i + tamanho_conjunto] for i in range(0, len(notas), tamanho_conjunto)]a

total_alunos = len(sublistas_notas)

notas_validas = [sublista for sublista in sublistas_notas if 0 not in sublista]

total_alunos_validos = len(notas_validas)

print(f"notas = {notas}")
print(f"O número total de alunos é {total_alunos}.")
print(f"O número de alunos com notas válidas é {total_alunos_validos}:")
print(notas_validas)
