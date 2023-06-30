jogador = dict()
partidas = list()
time = list()
total = 0
while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    jogos = int(input(f"Quantidade de jogos que {jogador['Nome']} jogou: "))
    for i in range(0,jogos):
        partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['Gols'] = partidas[:]
    # para pegar o total eu também poderia ter feito simplesmente:
    # jogador['total']=sum(partidas)
    for i in partidas:
        total = total + i
    jogador['Total'] = total
    time.append(jogador.copy())
# ========================== ^ LEITURA DE DADOS ^ ===================================
    while True:
        choice = str(input('Deseja continuar?[S/N] ')).upper()[0]
        if choice in 'NS':
            break
        else:
            print('Escolha incorreta!!')
    if choice == 'N':
        break
# ========================== ^ OPÇÃO PARA CONTINUAR ^ ===============================
print('=-'*20)
print(time)
print('=-'*20)
# indice
print(f'{"Cod "}',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
# valores
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    # d = dados
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existente jogador com código {busca}!')
    else:
        print(f"  ==  Levantamento do jogador {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print(f'      No jogo {i+1} fez {g} gols.')
        print('=-'*20)