from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    sleep(1)
    for i in range(0, 5):
        valores = randint(0, 10)
        print(valores, end=' ', flush=True)
        sleep(0.5)
        numeros.append(valores)
    print('Feito!')


def somaPar(par):
    soma = 0
    for i in par:
        if i % 2 == 0:
            soma += i
    print(f'Com a soma dos valores {par} temos {soma}')


# programa principal
numeros = list()
sorteia(numeros)
somaPar(numeros)
