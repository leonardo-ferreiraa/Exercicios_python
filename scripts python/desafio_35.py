r1 = float(input('digite o primeiro segmento'))
r2 = float(input('digite o segundo segmento'))
r3 = float(input('digite o terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível criar um triângulo')
else:
    print('Não é possível criar um triângulo')