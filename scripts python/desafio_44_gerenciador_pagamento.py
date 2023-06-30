#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJA '))
valor = int(input('Digite o valor do produto: '))

print('''Escolha uma das opções abaixo')
[ 1 ] a vista
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual opção você deseja: '))

if escolha == 1:
    total = valor - (valor * 10 / 100)
    print('Sua compra será a vista')
elif escolha == 2:
    total = valor - (valor * 5 / 100)
    print('Sua compra será a vista no cartão')
elif escolha == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x no cartão de R${:.2f}'.format(parcela))
elif escolha == 4:
    total = valor + ((valor * 20)/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('Escolha INCORRETA, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))