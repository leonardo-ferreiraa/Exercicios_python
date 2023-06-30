#Melhore o jogo do DESAFIO 28 onde
# o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('adivinhe o numero')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('qual é o número? :'))
    if jogador == computador:
        print('Acertou!!!')
        acertou = True
    elif jogador > computador:
        print('O número é menor...')
    elif jogador < computador:
        print('O número é maior...')
    palpites = palpites + 1
print('O jogador precisou de {} tentarivas'.format(palpites))
