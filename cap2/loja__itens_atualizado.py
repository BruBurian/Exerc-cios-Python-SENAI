itens = {
    "Café": 7,
    "Caneta": 3,
    "Copo de papel": 2,
    "Leite": 1,
    "Coca-Cola": 4,
    "Livro": 5
}

# Função para verificar o estoque de um item
def verificar_estoque(item):
    if item in itens:
        return itens[item]
    else:
        return None

# Função para armazenar mais unidades de um item no estoque
def armazenar_item(item, quantidade):
    if item in itens:
        itens[item] += quantidade
        return True
    else:
        return False

# Função para liberar unidades de um item do estoque
def liberar_item(item, quantidade):
    if item in itens and itens[item] >= quantidade:
        itens[item] -= quantidade
        return True
    else:
        return False

# Função principal para o menu
def menu():
    while True:
        print("\nSelecione uma opção:")
        print("1) Verificar estoque de um item")
        print("2) Armazenar mais unidades de um item")
        print("3) Liberar unidades de um item")
        print("4) Sair")
        
        opcao = input("Opção: ")

        if opcao == '1':
            item = input("Digite o nome do item: ")
            estoque = verificar_estoque(item)
            if estoque is not None:
                print(f"Estoque de {item}: {estoque}")
            else:
                print("Item não encontrado.")
        
        elif opcao == '2':
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade a armazenar: "))
            if armazenar_item(item, quantidade):
                print(f"{quantidade} unidades de {item} armazenadas com sucesso.")
            else:
                print("Item não encontrado.")
        
        elif opcao == '3':
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade a liberar: "))
            if liberar_item(item, quantidade):
                print(f"{quantidade} unidades de {item} liberadas com sucesso.")
            else:
                print("Estoque insuficiente ou item não encontrado.")
        
        elif opcao == '4':
            print("Programa encerrado.")
            break
        
        else:
            print("Opção inválida. Escolha novamente.")

# Chamada da função principal (menu)
menu()