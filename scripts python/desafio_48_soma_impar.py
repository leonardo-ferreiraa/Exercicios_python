soma = 0
valor = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
      soma = soma + c
      valor = valor + 1
print('a soma dos {} valores é: {}'.format(valor, soma))