n1 = int(input('digite o primeiro numero'))
n2 = int(input('digite o segundo numero'))
n3 = int(input('digite o terceiro numero'))

if n1 > n2 & n1 > n3:
    print('O primeiro número é maior que o segundo e o terceiro')
if n2 > n1 & n2 > n3:
    print('O segundo número é maior que o primeiro e o terceiro')
else:
    print('O terceiro número é maior que o segundo e o primeiro')
