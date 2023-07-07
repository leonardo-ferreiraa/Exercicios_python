from exerc108 import moeda

preco = float(input('Digite um preço: '))
print(f'O dobro do valor {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade do valor {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Com o aumento de 10%, temos {moeda.moeda(moeda.aumentar(preco,10))}')
print(f'Com o desconto de 10%, temos {moeda.moeda(moeda.diminuir(preco,10))}')

