#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo sem considerar espaços.
# Quantas letras tem o primeiro nome.
n = (input('digite o seu nome completo: '))
print (n)
print('Nome em maiusculo: {}'.format (n.upper()))
print('Nome em minusculo: {}'.format (n.lower()))
print('numero de letras ao todo: {}'.format (len(n)-n.count(' ')))
dividido = n.split()
print('Primeiro nome: {}'.format (dividido[0]))

