import random

resposta_correta = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

palpite = None

while palpite != resposta_correta:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite < resposta_correta:
        print("Seu palpite é menor que a resposta correta. Tente novamente.")
    elif palpite > resposta_correta:
        print("Seu palpite é maior que a resposta correta. Tente novamente.")
    else:
        print("Parabéns! Você acertou a resposta correta.")

