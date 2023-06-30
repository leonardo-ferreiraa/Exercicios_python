#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
print("-"*28)
print("-Análise de dados de grupos-")
print("-"*28)
cont = cont_m = cont_f = 0
while True:
    print("-="*10)
    idade = int(input("Digite a sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Digite o seu sexo: M/F: ").upper()
    print("-="*10)
    if idade > 18:
        cont += 1
    if sexo == "M":
        cont_m += 1
    if sexo == "F":
        if idade > 20:
            cont_f += 1
    escolha = " "
    while escolha not in "SN":
        escolha = input("Deseja continuar? S/N:").upper()
    if escolha == "N":
        break
print(f"Existe {cont} pessoas com mais de 18 anos cadastrados")
print(f"Foram cadastrados {cont_m} homem(ns) cadastrados")
print(f"Existe {cont_f} mulheres com mais de 20 anos cadastrados")