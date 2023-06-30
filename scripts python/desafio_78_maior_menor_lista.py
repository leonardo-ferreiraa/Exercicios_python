# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listaval = []
maior = 0
menor = 0
for c in range(0, 5):
    listaval.append(int(input(f"digite o {c}º valor: ")))
    if c == 0:
        menor = maior = listaval[c]
    if listaval[c] > maior:
        maior = listaval[c]
    if listaval[c] < menor:
        menor = listaval[c]
print(f"lista: {listaval}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for posicao, valor in enumerate(listaval):
    if valor == maior:
        print(f"{posicao}... ", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for posicao, valor in enumerate(listaval):
    if valor == menor:
        print(f"{posicao}... ", end="")
