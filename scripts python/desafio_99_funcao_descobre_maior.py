from time import sleep


def maior(* num):
    maior = count = 0
    print('-' * 30)
    for valor in num:
        print(f'{valor} ', end='',flush=True)
        sleep(0.5)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'foram informados {len(num)} valores')
    print(f'O maior número informado é {maior}')
    print('-'*30)


# programa principal
maior(5, 2, 4, 7, 1, 6)
maior(7, 2, 1)
maior(5, 2)
maior(1)
maior()
