#esse 2 no final do laço de repetição serve para ele pular de 2 em 2
for c in range(2, 51, 2):
    print('{} '.format(c), end=(''))
#se usar o if ele fará 2 laços, assim ocupando espaço atoa no processador, EX: 2.. 4.. 8.. etc
#if c % 2 == 0:
print ('fim')