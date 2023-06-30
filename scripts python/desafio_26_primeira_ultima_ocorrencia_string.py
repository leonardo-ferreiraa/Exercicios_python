frase = str(input('Digite uma frase: ')).upper()
print('A quantidade de letras A é: {}'.format(frase.count('A')))
print('A primeira letra A está na posição: {}'.format(frase.find('A')))
print('A última letra A está na posição: {}'.format(frase.rfind('A')))