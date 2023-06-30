#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = int(input('digite o valor da casa: '))
salario = int(input('digite o seu salário: '))
ano = int(input('digite a prestação mensal: '))
prestacao = casa / (ano * 12)
minimo = salario * 30 / 100
print('Para pagar a casa de R${:.2f} com um salário de R${:.2f} em {} anos'.format(casa, salario, ano))
print('a prestação custará R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('O empréstimo pode ser concedido')
else:
    print('O empréstimo foi NEGADO')