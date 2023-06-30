t = int(input('Quantos dias Alugados?'))
d = int(input('Quantos km rodados?'))
resultado = (t * 60) + (d * 0.15)
print('O total a pagar é de R${}'.format(resultado))