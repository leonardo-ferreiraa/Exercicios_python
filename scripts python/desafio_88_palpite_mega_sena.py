from random import randint
jogos = []
palpites = []
jogos_sorteados = int(input("Quantos jogos você quer sortear? "))
for i in range(0, jogos_sorteados):
    count = 0
    while True:
        numero = randint(0, 60)
        if numero not in palpites:
            palpites.append(numero)
            count += 1
        if count >= 6:
            break
    jogos.append(palpites[:])
    palpites.clear()
for i in range(0,jogos_sorteados):
    print(sorted(jogos[i]))