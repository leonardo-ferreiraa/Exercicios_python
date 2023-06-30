#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = n = total = 0
#quando coloca != ele irá entender que se for diferente de 999 ele repete e se for igual ele para
while n != 999:
    total += 1
    n = int(input("Digite um valor: (para em 999)"))
    soma += n
    if n == 999:
        soma -= 999
        total -= 1
print(" a quantidade de números digitados foi {} e a soma de todos é: {}".format(total, soma))
