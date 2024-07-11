def string_longa(lista):
  string = lista[0]
  for i in range(1, len(lista)):
    if len(lista[i]) > len(string):
      string = lista[i]
  return string

# Lista de strings de exemplo
lista = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

string = string_longa(lista)
print(f"A string mais longa: {string}")