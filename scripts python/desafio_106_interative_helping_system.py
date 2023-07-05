from time import sleep
c = ('\033[m',         # 0 sem cor
     '\033[0;30;41m',   # vermelho
     '\033[40;32m',     # verde com fundo preto
     '\033[47;30m',     # preto com fundo branco
     '\033[44m'      # branco com fundo azul
     )


def ajuda(com):
    titulo(f'acessando o manual do comando \'{com}\'', 4)
    print(c[3])
    (help(com))
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(2)


# programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
