def aumentar(valor, taxa):
    total = valor + (valor * taxa / 100)
    return f'Aumento de {taxa}%, temos R${total:.2f}'


def diminuir(valor, taxa):
    total = valor - (valor * taxa / 100)
    return f'desconto de {taxa}%, temos R${total:.2f}'


def dobro(valor):
    total = valor*2
    return f'O dobro do valor R${valor} é R${total:.2f}'


def metade(valor):
    total = valor/2
    return f'A metade do valor R${valor} é R${total:.2f}'
