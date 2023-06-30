#Escreva um programa em Python que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
conversao = int(input('digite o número que deseja converter: '))
print('[1] para converter em binário')
print('[2] para converter em octal')
print('[3] para converter em hexadecimal')
escolha = int(input('opção desejada: '))
if escolha == 1:
    print('O número {} convertido para binário é: {}'.format(conversao, bin(conversao)))
elif escolha == 2:
    print('O número {} convertido para octal é: {}'.format(conversao, oct(conversao)))
elif escolha == 3:
    print('O número {} convertido para hexadecimal é: {}'.format(conversao, hex(conversao)))
else:
    print('escolha inválida')
