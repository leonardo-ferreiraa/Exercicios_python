boletim = {}
boletim['Nome'] = input('Nome do aluno: ')
boletim['Média'] = float(input('Media do aluno: '))
if boletim['Média'] >= 6.0:
    boletim['situaÇão'] = 'aprovado'
elif boletim['Média']>= 3.5:
    boletim['situaÇão'] = 'recuperação'
else:
    boletim['situaÇão'] = 'reprovado'
print('-='*30)
for v, k in boletim.items():
    print(f'- {v} é igual a {k}')