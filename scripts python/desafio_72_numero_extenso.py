numero = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez",
          "onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
    escolha = int(input("Escolha um número: "))
    if escolha <= 20:
        break
    else:
        print("Escolha inválida!")
print("Você escolheu o número {}".format(numero[escolha]))