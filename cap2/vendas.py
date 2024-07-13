vendas_diarias = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)

dias_com_queda_nas_vendas = 0

for i in range(1, len(vendas_diarias)):
  if vendas_diarias[i] < vendas_diarias[i - 1]:
    dias_com_queda_nas_vendas += 1

print("Nos ultimos 10 dias tiveram", dias_com_queda_nas_vendas, "dias com queda em relação ao dia anterior")