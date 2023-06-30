jogador = dict()
partidas = list()
total = 0
jogador['nome'] = input('Nome do jogador: ')
jogos = int(input(f"Quantidade de jogos que {jogador['nome']}: "))
for i in range(0,jogos):
    partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = partidas[:]
# para pegar o total eu também poderia ter feito simplesmente:
# jogador['total']=sum(partidas)
for i in partidas:
    total = total + i
jogador['total'] = total
print('=-'*20)
print(jogador)
print('=-'*20)
for v, k in jogador.items():
    print(f'O campo {v} tem o valor {k}')
print('=-'*20)
# o len(jogador['gols']) serve para ele ser a quantidade de gols que é
# respectivamente a quantidade de jogos jogados sem usaor a variavel jogos
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i+1}, fez {v} gols.')
print(f"foi um total de {jogador['total']} gols")