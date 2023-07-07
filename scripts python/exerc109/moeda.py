def aumentar(valor=0, taxa=0, formato=False):
    """
    -> Função para aumentar a taxa do valor passado
    :param valor: valor passado(deve ser Float)
    :param taxa: quanto % o valor foi aumentado
    :param formato: puxa a função formato Moeda
    :return: retorna o valor aumentado
    """
    total = valor+(valor*taxa/100)
    # se o format for igual a false senão vou retornar o moeda(preco)
    #
    return total if formato is False else moeda(total)


def diminuir(valor=0, taxa=0, formato=False):
    """
    -> Função para diminuir a taxa do valor passado
    :param valor: valor passado(deve ser Float)
    :param taxa: quanto % o valor foi diminuido
    :param formato: puxa a função formato Moeda
    :return:  retorna o valor diminuido
    """
    total = valor-(valor*taxa/100)
    return total if formato is False else moeda(total)


def dobro(valor=0, formato=False):
    """
    -> Função para dobrar o valor passado
    :param valor: valor passado(deve ser Float)
    :param formato: puxa a função formato Moeda
    :return: retorna o valor dobrado
    """
    total = valor*2
    return total if formato is False else moeda(total)


def metade(valor=0, formato=False):
    """
    -> Função para dividir pela metade o valor passado
    :param valor: valor passado(deve ser float)
    :param formato: puxa a função formato Moeda
    :return: retorna o valor dividido pela metade
    """
    total = valor/2
    return total if formato is False else moeda(total)


def moeda(preco=0, moeda='R$'):
    """
    -> Função para formatar no formato moeda
    :param preco: Valor passado(deve ser float)
    :param moeda: O tipo de moeda
    :return: retorna o valor formatado no tipo de moeda especificada
    """
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')
