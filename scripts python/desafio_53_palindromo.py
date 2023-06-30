frase = str(input('Digite uma frase: ')).strip().upper()
#separa as palavras criando uma lista
palavras = frase.split()
# junta a lista
junto = ''.join(palavras)
#auxiliar para mostrar o inverso da palavra
inverso = ''
#o len é para contar as letras da frase começando da direita
# o primeiro -1 vai pegar o numero de letras do junto e tirar 1 para contar corretamente todas as letras
#vai até a letra -1 que é antes da primeira
# o último -1 é que vai voltando uma letra
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('é palíndromo')
else:
    print('não é palíndromo')