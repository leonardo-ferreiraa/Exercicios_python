#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
r1 = int(input('digite o primeiro segmento: '))
r2 = int(input('digite o segundo segmento: '))
r3 = int(input('digite o terceio segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode formar um triângulo')
elif r1 == r2 == r3:
    print('EQUILÁTERO!')
elif r1 != r2 != r3:
    print('ESCALENO!')
else:
    print('Não é possível formar nenhum dos 3 triângulos')