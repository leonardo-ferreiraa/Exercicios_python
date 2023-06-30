# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = contador = total = maior = menor = 0
escolha =""
while escolha in "S":
    n = int(input("Digite um número: "))
    total += n
    #contador servirá para saber quantas vezes repetiu para tirar a média
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    escolha = (input("Deseja continuar?[S/N]")).upper()
media = total / contador
print("A média dos {} digitados foi: {}".format(contador, media))
print("o maior valor lido foi: {}".format(maior))
print("O menor valor lido foi: {}".format(menor))