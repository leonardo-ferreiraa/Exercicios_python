cont = 0
soma = 0
while True:
    n = int(input("digite um número: "))
    if n == 999:
        break
    cont += 1
    soma = soma + n
print(f"foi digitado {cont} números")
print(f"A soma de todos vale {soma}")
