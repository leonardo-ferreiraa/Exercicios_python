lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    choice = str(input('Quer continuar? [S/N] ')).upper()
    if choice == "N":
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores digitados em ordem crescente foram {lista}')
