def determinar_quadrante(x, y):
  if x > 0 and y > 0:
    quadrante = 1
  elif x < 0 and y > 0:
    quadrante = 2
  elif x < 0 and y < 0:
    quadrante = 3
  else:
    quadrante = 4

  return quadrante

x = int(input("Escreva o ponto X: "))
y = int(input("Escreva o ponto Y: "))


quadrante = determinar_quadrante(x, y)

print(f"O ponto ({x}, {y}) está no quadrante {quadrante}")