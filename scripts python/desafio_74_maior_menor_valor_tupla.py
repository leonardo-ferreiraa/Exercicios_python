#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
#ao colocar o randint(1,10) dentro de parenteses eles se tornam uma tupla
#com isso só repetir o processo mais vezes para ter números aleatorios dentro de uma tupla
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print("os número sorteados foram:", end=' ')
for n in numeros:
    print(f"{n}", end=' ')
print(f"\nO maior número é {max(numeros)}")
print(f"O menor número é {min(numeros)}")