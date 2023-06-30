#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
resultado_final = ""
vitorias = 0
print("-=" * 10)
print("Jogo de par ou impar")
print("-=" * 10)
while True:
    bot = randint(1, 10)
    escolha = (input("\nFaça uma escolha [P/I]: ")).upper()
    if escolha == "P":
        escolhacomput = "I"
    if escolha == "I":
        escolhacomput = "P"
    player = int(input("Digite um número entre 0 a 10: "))
    soma = player + bot
    resultado = soma % 2
    if escolha == "I" and resultado != 0:
        resultado_final = "WIN"
    if escolha == "I" and resultado == 0:
        resultado_final = "LOSE"
    if escolha == "P" and resultado != 0:
        resultado_final = "LOSE"
    if escolha == "P" and resultado == 0:
        resultado_final = "WIN"
    vitorias += 1
    if resultado_final == "LOSE":
        break
    print("-"*20)
    print(f"Você jogou {player} e o bot jogou {bot}, o resultado foi {resultado}")
    print("-"*20)
    print("você VENCEU!!")
    print("Vamos jogar novamente!")
print(f"Você jogou {player} e o bot jogou {bot}, o resultado foi {resultado}")
print(f"você PERDEU!!, obteve um total de {vitorias} vitórias")
