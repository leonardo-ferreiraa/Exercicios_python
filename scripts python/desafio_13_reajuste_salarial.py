valor = float(input('Salário do funcionário:'))
aumento = valor + (valor * 0.15)
print('O salário do funcionário que era R${}, com 15% de aumento começou a receber R${:.2f}'.format(valor, aumento))