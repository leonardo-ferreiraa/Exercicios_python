#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
#valor do saque que será digitado
valor = int(input("Digite o valor do saque: "))
#célula de dinheiro
total = valor
cel = 50
totcel = 0
while True:
    #enquanto o valor for maior que a célula
    # ele irá fazer o valor menos a célula e
    # o adicionará 1 célula de 50 reais
    if total >= cel:
        total -= cel
        totcel += 1
    else:
        if totcel > 0:
            print(f"total de {totcel} célula(s) de R${cel} ")
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        totcel = 0
        if total == 0:
            break

