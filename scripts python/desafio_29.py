velocidade = int(input('digite a velocidade: '))
if velocidade > 80:
    print('você ultrapassou a velocidade')
    multa = (velocidade - 80) * 7
    print('você receberá uma multa de R${}'.format(multa))
else:
    print('você está dentro do limite')