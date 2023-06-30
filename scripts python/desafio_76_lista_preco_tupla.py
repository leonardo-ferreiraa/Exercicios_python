#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ("lápis", 1.75,
"Borracha", 2.00,
"Caderno", 15.00,
"Estojo", 25.00,
"Transferidor", 4.20,
"Compasso", 9.99,
"Mochila" ,120.32,
"Canetas", 22.30,
"Livros", 34.90)
print("="*30)
print((f'{"PREÇOS":^30}'))
print("="*30)
for pos, lista in enumerate(produtos):
    if pos % 2 == 0:
        print(f"{lista:.<20}",end=" ")
    else:
        print(f"R$ {lista:>6}")
print("="*30)
