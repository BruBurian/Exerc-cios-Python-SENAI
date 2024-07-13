itens = {
    "Café": 7,
    "Caneta": 3,
    "Copo de papel": 2,
    "Leite": 1,
    "Coca-Cola": 4,
    "Livro": 5
}

nome_item = input("Digite o nome do item: ")

if nome_item in itens:
    print(itens[nome_item])
else:
    print("Item não disponível.")