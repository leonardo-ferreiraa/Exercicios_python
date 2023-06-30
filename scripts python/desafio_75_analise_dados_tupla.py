#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
valores = (int(input("Digite o 1º valor: ")),
           int(input("Digite o 2º valor: ")),
           int(input("Digite o 3º valor: ")),
           int(input("Digite o 4º valor: ")))
# para procurar o número ou palavra em específico deve se colocar: variavel.count(valor/palavra)
print(f"O valor 9 apareceu {valores.count(9)} vezes")
print(f"O primeiro valor 3 foi digitado na {valores.index(3)+1}º posição")
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
print("são os número pares")
print(valores)

