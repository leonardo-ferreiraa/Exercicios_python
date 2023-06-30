#lista única com duas listas dentro
lista = [[],[]]
valor = 0
i = 0
valor = 0
for i in range(1,8):
    valor = int(input(f"digite o {i}º valor: "))
    #número de pares digitados
    if valor % 2 == 0:
        lista[0].append(valor)
    #número de ímpares digitados
    else:
        lista[1].append(valor)
print(f"lista de valores digitados {lista}")
#irá ordernar os valores para ordem crescente
print(f"números pares digitados: {sorted(lista[0])}")
print(f"números ímpares digitados: {sorted(lista[1])}")