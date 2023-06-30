#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano
if idade < 18:
    cedo = 18 - idade

    print('Você ainda irá se alistar daqui a {} anos'.format(cedo))
    dia_alist = ano + 18
    print('O seu alistamento foi no ano de {}'.format(dia_alist))
elif idade > 18:
    tarde = idade - 18
    print('Você devia ter se alistado a {} anos atrás'.format(tarde))
    dia_alist = ano + 18
    print('O seu alistamento foi no ano de {}'.format(dia_alist))
else:
    print('Você está dentro do prazo de se alistar ao serviço militar')
    print('Não perca tempo!!')
    dia_alist = ano + 18
    print('O seu alistamento foi no ano de {}'.format(dia_alist))