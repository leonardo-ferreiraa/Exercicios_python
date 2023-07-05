def fatorial(n,show=False):
    """
    Calcula o Fatorial de um número
    :param n:número a ser calculado
    :param show:(opcional) mostrar ou não a conta
    :return:O valor Fatorial de um número n
    """
    v = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ' ,end='')
        v *= i
    return v


help(fatorial)
print(fatorial(5, show=False))
#print(fatorial(5, show=True))
