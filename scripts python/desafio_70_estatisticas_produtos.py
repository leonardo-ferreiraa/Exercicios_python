#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = cont1000 = cont = menor = 0
barato = " "
print("="*20)
print("=  Super mercado   =")
print("="*20)
while True:
    cont += 1
    produto = input("Cadastre o nome do produto: ")
    preco = int(input("Cadastre o valor do produto: R$"))
    total += preco
    if preco > 1000:
        cont1000 += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    escolha = " "
    while escolha not in "SN":
        escolha = input("Irá continuar? [S/N]: ").upper()
    if escolha == "N":
        break
print(f"O total de gasto na compra foi R${total}")
print(f"Existe {cont1000} produtos que custam mais de R$1000,00")
print(f"O produto mais barato é {barato} que custa R${menor}")