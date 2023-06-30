#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
print('Fatorial')
n1 = int(input('Digite o número: '))
x = False
R = 1
aux = 0
while not x:
    aux = aux + 1
    R = R * aux
    if aux == n1:
        x = True
print('O resultado do fatorial de {}! é: {}'.format(n1 ,R))