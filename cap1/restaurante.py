def main():
    print("Bem-vindo ao Restaurante Yummy!")
    print("Aqui está o nosso cardápio:")
    print("• Hambúrguer (digite H)")
    print("• Frango (digite F)")
    print("• Pizza (digite P)")

    escolha = input("Escolha um item do menu (H, F ou P): ").upper()

    while escolha not in ["H", "F", "P"]:
        escolha = input("Entrada inválida. Escolha um item do menu (H, F ou P): ").upper()

    preco_item = 0

    if escolha == "H":
        preco_item = 25.00
    elif escolha == "F":
        preco_item = 30.00
    elif escolha == "P":
        preco_item = 35.00

    total = preco_item

    print("\nRecibo:")
    print(f"Item: {escolha}")
    print(f"Preço do item: R${preco_item:.2f}")
    print(f"Total: R${total:.2f}")

    print("\nObrigado pelo seu pedido!")

if __name__ == "__main__":
    main()
