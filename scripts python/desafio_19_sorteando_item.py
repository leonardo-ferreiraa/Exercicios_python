import random
al1 = str(input('digite o nome do primeiro aluno:'))
al2 = str(input('digite o nome do segundo aluno:'))
al3 = str(input('digite o nome do terceiro aluno: '))
al4 = str(input('digite o nome do quarto aluno: '))
print('o número sorteado da lista foi: ')
lista = [al1, al2, al3, al4]
sorteado = random.choice(lista)
print('o aluno sorteado foi:{}'.format(sorteado))