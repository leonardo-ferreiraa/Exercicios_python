lista = list()
count = 0
while True:
    nome = (input("Nome: "))
    nota1 = (float(input("nota 1: ")))
    nota2 = (float(input("nota 2: ")))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    count += 1
    choice = input("Deseja continuar? [N/S]").upper()
    if choice == "N":
        break
print("-="*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-"*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-"*60)
    escolha = int(input("Mostrar notas de qual aluno? (999 finaliza a operação): "))
    if escolha == 999:
        break
    if escolha<=len(lista) -1:
        print(f"Notas de {lista[escolha][0]} são{lista[escolha][1]}")
"""
dados = []
lista = []
count = 0
while True:
    dados.append(count)
    dados.append(input("Nome: "))
    dados.append(float(input("nota 1: ")))
    dados.append(float(input("nota 2: ")))
    lista.append(dados[:])
    dados.clear()
    count += 1
    choice = input("Deseja continuar? [N/S]").upper()
    if choice == "N":
        break
print("")
for i in range(0, count):
    for j in range(0,2):
        print(f"{lista[i][j]:^8}",end='')
    media = (lista[i][2] + lista[i][3]) / 2
    print(f"Média: {round(media, 1)}")
while True:
    print("-"*60)
    escolha = int(input("Mostrar notas de qual aluno? (999 finaliza a operação): "))
    if escolha == 999:
        break
    print(f"As notas de {lista[escolha][1]} são [{lista[escolha][2]} , {lista[escolha][3]}]")
"""