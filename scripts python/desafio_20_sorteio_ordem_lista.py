import random
A1 = input('Primeiro Aluno:')
A2 = input('Segundo Aluno:')
A3 = input('Terceiro Aluno:')
A4 = input('Quarto Aluno:')
lista = [A1,A2,A3,A4]
#randomiza a lista
random.shuffle(lista)
print('Ordem de apresentação será')
print(lista)

