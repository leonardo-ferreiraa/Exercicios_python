def notas(*n, sit=False):
    '''
    -> Função para analisar notas de vários alunos e mostrar sua situação
    :param n: Armazena uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não mostrar ou não a situação dos alunos
    :return: dicionário com várias informações sobre a situação da turma
    '''
    turma = dict()
    turma['Total'] = n
    turma['Maior'] = max(n)
    turma['Menor'] = min(n)
    turma['Media'] = sum(n)/len(n)
    print(f'{turma} ', end='')
    if sit:
        if turma['Media'] >= 6:
            return 'estado: APROVADOS'
        elif turma['Media'] >= 4.5:
            return 'estado: RECUPERACAO'
        else:
            return 'estado: REPROVADOS'


# programa principal
resp = notas(9.5, 4.1, 6.5, 10, sit=True)
print(resp)
help(notas)
