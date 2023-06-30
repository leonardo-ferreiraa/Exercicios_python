n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(nome[0])
#nome[é colocado len para ler as posições e o -1 para não contar o 0]
print(nome[len(nome)-1])