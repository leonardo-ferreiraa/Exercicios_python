import datetime
specific_datetime = datetime.date.today()
ano_atual = specific_datetime.year


def voto(v):

    if idade < 16:
        return 'NÃO OBRIGATÓRIO'
    elif idade <= 70:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'



ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano
print(f'Com {idade} anos: VOTO {voto(idade)}')