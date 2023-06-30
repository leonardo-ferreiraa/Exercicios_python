#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = int(input('Digite o seu peso (Kg) : '))
altura = int(input('Digite a sua altura  (m) : '))
massa = peso / (altura * altura)
if massa < 18.5:
    print('abaixo do peso')
elif 18.5 >= massa < 25:
    print('Peso Ideal')
elif 25 >= massa < 30:
    print('Sobrepeso')
elif 30 >= massa <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')