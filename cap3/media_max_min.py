def media3(a, b, c):
  return (a + b + c) / 3

def max3(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c

def min3(a, b, c):
  if a <= b and a <= c:
    return a
  elif b <= a and b <= c:
    return b
  else:
    return c

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

media = media3(a, b, c)
maximo = max3(a, b, c)
minimo = min3(a, b, c)

print(f"O valor médio de {a}, {b}, {c} é {media:.6f}")
print(f"O valor máximo de {a}, {b}, {c} é {maximo}")
print(f"O valor mínimo de {a}, {b}, {c} é {minimo}")