print('Gerador de PA')
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão de PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo +=razao
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos deseja mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
print("Fim")