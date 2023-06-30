from random import randint
from time import sleep
item = ('PEDRA','PAPEL','TESOURA')
bot = randint(1, 3)
print('{:=^40}'.format('JOGO PEDRA PAPEL TESOURA'))
print('''Escolha uma opção:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
player = int(input('Opção desejada: '))
print('O bot está escolhendo')
sleep(3)
print('-='*12)
print('O jogador jogou {}'.format(item[player]))
print('O bot jogou {}'.format(item[bot]))
print('-='*12)
if player == 1:
    if bot == 1:
        print('Empate!')
    elif bot == 2:
        print('\033[0:31mVITORIA do bot!\033[m')
    else:
        print('\033[0:32mVITORIA do player!\033[m')
elif player == 2:
    if bot == 1:
        print('\033[0:32mVITORIA do player!\033[m')
    elif bot ==2:
        print('Empate!')
    else:
        print('\033[0:31mVITORIA do bot!\033[m')
elif player == 3:
    if bot == 1:
        print('\033[0:31mVITORIA do bot!\033[m')
    elif bot == 2:
        print('\033[0:32mVITORIA do player!\033[m')
    else:
        print('Empate!')
