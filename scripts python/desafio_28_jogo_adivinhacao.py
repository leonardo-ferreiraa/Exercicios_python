
from random import randint
computador = randint(0, 5)
print('adivinhe o numero')
jogador = int(input('qual é o número?'))
if jogador == computador:
    print('acertou')
else:
    print('errou, o número certo é: {}'.format (computador))