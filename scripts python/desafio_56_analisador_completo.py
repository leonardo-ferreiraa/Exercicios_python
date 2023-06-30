#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
maior = 0
maioridadehomem= 0
homem_nome =''
totmulher = 0
for c in range(1, 5):
    print('----- {}ºPESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homem_nome = nome
    if sexo in 'Ff' and idade < 20:
        totmulher +=1
media_grupo = somaidade / 4
print('A média da idade do grupo é {}anos'.format(media_grupo))
print('O nome do homem de {} anos mais velho é {}'.format(maioridadehomem,homem_nome))
print('A quantidade de mulheres com menos de 20 anos é {} mulher(es)'.format(totmulher))

