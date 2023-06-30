#faça um programa que leia o comprimento do cateto o posto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da ipotenusa
import math
print('Desafio 17')
print('faça um programa que leia o comprimento do cateto o posto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da ipotenusa:')
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjasente: '))
#I = math.hypot(co, ca)
I = (co ** 2 + ca ** 2) ** (1/2)
print('O resultado do triângulo retângulo é: {}'.format(I))