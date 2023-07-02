from time import sleep
#NÃO FINALIZADO, fiquei perdido


def contador(a, b, c):
    print('-'*30)
    print(f'Contadem de {a} até {b} de {c} em {c}')
    sleep(2.5)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            # o flush serve para que caso ocorra o problema de os sleeps se juntarem em um só o flush concerta
            print(cont, end=' ', flush=True)
            sleep(0.25)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(cont, end=' ', flush=True)
            sleep(0.25)
            cont -= c
        print('FIM!')
    print('-' * 30)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize a contagem!')
ini = int(input('Inicio: '))
fim = int(input('FIM:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
