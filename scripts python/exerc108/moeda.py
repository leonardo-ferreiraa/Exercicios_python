def aumentar(valor=0, taxa=0):
    total = valor+(valor*taxa/100)
    return total


def diminuir(valor=0, taxa=0):
    total = valor-(valor*taxa/100)
    return total


def dobro(valor=0):
    total = valor*2
    return total


def metade(valor=0):
    total = valor/2
    return total


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')
