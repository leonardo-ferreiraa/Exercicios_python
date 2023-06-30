from time import sleep
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor: '))
condicao = False
while not condicao:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair')
    escolha = int(input('opção: '))
    if escolha == 1:
        R = n1 + n2
        print('O resultado da soma é: {}'.format(R))
    elif escolha == 2:
        R = n1 * n2
        print('O resultado da multiplicação é: {}'.format(R))
    elif escolha == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O entre o número {} e {} o maior número é {}'.format(n1, n2, maior))
    elif escolha == 4:
        print('Por favor digite os valores novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('finalizando...')
        sleep(3)
        condicao = True
    else:
        print('opção incorreta, por favor digite novamente.')
    print('-='*20)



