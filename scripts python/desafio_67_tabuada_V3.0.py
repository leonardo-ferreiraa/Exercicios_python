#Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    cont = 0
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("=" * 20)
    while cont != 10:
        cont += 1
        r = n * cont
        print(f"{n} X {cont} = {r}")
    print("=" * 20)
print("TABUADA ENCERRADA")