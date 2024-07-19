from random import randint
import sys

dezenas = 6

def existeNumero(numeros, n):
    return n in numeros

def acertos(sorteio, aposta):
    global dezenas
    acertos = 0
    for i in range(0, dezenas):
        numAposta = aposta[i]

        if (existeNumero(sorteio, numAposta)):
            acertos += 1

    return acertos

def sorteia():
    global dezenas
    resultado = []

    for i in range(0, dezenas):
        repetido = []

        while True: 
            sorteado = randint(1, 60)
            if not existeNumero(resultado, sorteado):
                break

        resultado.append(sorteado)

    return resultado

sorteio = sorteia()
aposta = []

for i in range (0, dezenas):

    while True:
        numAposta = int(input("Informe a dezena "+ str(i+1) +": "))
        if (numAposta <= 0):
            print ("Número inválido, aposta cancelada!")
            sys.exit(); # encerra o programa

        if (existeNumero(aposta, numAposta)):
            print ("Ops, número repetido!")
        else:
            break

    aposta.append(numAposta)

print("\nConfira sua aposta: ", str(aposta)[1:-1])

print("\nResultado do sorteio: ", str(sorteio)[1:-1])

numAcertos = acertos(sorteio, aposta)

print("\nNúmero de acertos: ", numAcertos)

if numAcertos == 4:
    print("Parabéns. Você acertou a quadra!")
elif numAcertos == 5:
    print("Parabéns. Você acertou a quina!")
elif numAcertos == 6:
    print("Parabéns. Você é campeão da MegaSena!")
else:
    print("Não foi dessa vez. Tente novamente!")
