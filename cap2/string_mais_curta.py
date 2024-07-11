def menor_string(lista):
  string = lista[0]
  for i in range(1, len(lista)):
    if len(lista[i]) < len(string):
      string = lista[i]
  return string

# Lista de strings de exemplo
lista = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

# Chamada da função para encontrar a string mais curta
string = menor_string(lista)

# Impressão da string mais curta
print(f"A string mais curta: {string}")