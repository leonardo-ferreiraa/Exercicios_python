from exerc109 import moeda

preco = float(input('Digite um preço: '))
print(f'O dobro do valor {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade do valor {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Com o aumento de 10%, temos {moeda.aumentar(preco,10, True)}')
print(f'Com o desconto de 10%, temos {moeda.diminuir(preco,13, True)}')

