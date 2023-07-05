def ficha(n='<desconhecido>', g=0):
    '''
    Ficha de jogador
    :param n: nome do jogador
    :param g: número de gols
    :return: false
    '''
    print(f'O jogador {n} fez {g} gols(s) no campeonato')


nome = str(input('Nome do jogador: '))
gol = str(input('Quantidade de gols: '))
# se for numérico: gol torna=se inteiro
if gol.isnumeric():
    gol = int(gol)
# se não, vira 0
else:
    gol = 0
# se o nome não tiver nada, o g recebe gol
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)
help(ficha)
