#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distância = int(input('digite a distância em Km: '))
if distância <= 200:
  valor =  distância * 0.50
  print('o valor total será: R${}'.format(valor))
else:
  valor = distância * 0.45
  print('o valor total será: R${}'.format(valor))