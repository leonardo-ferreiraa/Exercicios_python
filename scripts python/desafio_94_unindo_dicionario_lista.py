pessoa = dict()
galera = list()
choice = ''
soma = media = 0
# enquanto a escolha não é igual a N, continua
while not choice == 'N':
    # comando para limpar o dicionário quando a repetição ocorrer
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    # Condição serve para verificar se o usuario digitou corretamente M ou F
    while True:
        pessoa['sexo'] = str(input('[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Escolha incorreta!! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    # soma das idades
    soma += pessoa['idade']
    # comando criar uma cópia dentro da lista
    galera.append(pessoa.copy())
    choice = input('Quer continuar? [S/N]').upper()[0]
    # Condição serve para verificar se o usuario digitou corretamente S ou N
    while True:
        if choice in 'SN':
            break
        choice = input('Escolha incorreta!! Digite apenas S ou N: ').upper()
# ========================== ^ LEITURA DE DADOS ^ ===================================
print('-='*40)
print(f'A) Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'B) a média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f"[{p['nome']}]",end='')
print()
print('D) lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
    print()
print('==ENCERRADO==')