lista = []
pessoas = []
maior = menor = 0
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    if len(pessoas)== 0:
        maior = menor = lista[1]
    else:
        # maior e menor número
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    choice = input("Deseja continuar? [S/N]: ").upper()
    if choice == "N":
        break
print(f"lista: {pessoas}")
print(f"você cadastrou {len(pessoas)} pessoas")
print(f"O maior peso foi de {maior}Kg de", end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
print()
print(f"O menor peso foi de {menor}Kg de", end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')