lista = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
maior = 0
valor_coluna = 0
for l in range(0, 3):
    for c in range(0,3):
        # O formato l e c é para poder substituir os zero, eu poderia fazer sem os zeros também mas quiz seguir o video a risca
        lista[l][c] = (int(input(f"Digite o valor para [{l}:{c}]: ")))
        # maior da segunda linha
        if l == 1:
            if c == 0:
                maior = lista[l][c]
            # verifica qual valor da segunda linha é maior
            if lista[l][c] > maior:
                maior = lista[l][c]
        # soma dos pares
        if lista[l][c] % 2 == 0:
            soma = soma + lista[l][c]
        # soma da terceira coluna
        if c == 2:
            valor_coluna = valor_coluna + lista[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        #O :^5 é utilizado para centralizar com 5 casas decimais
        print(f'[{lista[l][c]:^5}]',end='')
    print()
print(f"A soma dos números pares deu {soma}")
print(f"A soma da terceira coluna é de {valor_coluna}")
print(f"O maior valor da segunda linha é {maior}")