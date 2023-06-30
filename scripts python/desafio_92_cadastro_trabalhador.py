import datetime
from time import sleep
usuario = dict()
# pega a data atual de hoje
specific_datetime = datetime.datetime.today()
# comando serve para pegar o dia, mes, ano especifico desejados
year = specific_datetime.year
usuario['Nome'] = input('Nome:')
data_nasc = int(input('Ano de nascimento:'))
# eu poderia fazer também
# datetime.now().year = data_nasc
usuario['Idade'] = year - data_nasc
usuario['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver):'))
if usuario['CTPS'] != 0:
    usuario['Contratação'] = int(input('Ano de contratação:'))
    usuario['Salário'] = float(input('Salário: R$'))
    usuario['Aposentadoria'] = usuario['Idade'] +35
print('-='*20)
for v, k in usuario.items():
    print(f'- {v} tem o valor {k}.')
    sleep(1)
