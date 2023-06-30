#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela
lista = []
for c in range(0, 5):
    numero= int(input(f"Digite um número: "))
    # se o número foi maior que o número que está no último elemento
    # para pegar o último elemento len(variavel)-1 ou lista[-1]
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print("adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(f"{lista}")