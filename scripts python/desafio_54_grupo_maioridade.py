from datetime import date
jovem = 0
maioridade = 0
data_atual = date.today().year
for c in range(1, 7 + 1):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if data_atual - ano <=18:
        jovem = jovem + 1
    else:
        maioridade =maioridade + 1
print('existem {} pessoas que são jovens e {} pessoas que são maioridade'.format(jovem, maioridade))
