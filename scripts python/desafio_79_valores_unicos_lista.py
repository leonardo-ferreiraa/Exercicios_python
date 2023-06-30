#Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
cont = 0
while True:
    cont += 1
    n = int(input(f"digite o {cont} valor: "))
    if n not in lista:
        lista.append(n)
    condicao = input("Deseja continuar? [S/N]: ")
    if condicao in 'Nn':
        break
lista.sort()
print(lista)
