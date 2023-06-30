preco = float(input('Digite o preço do produto: R$'))
resultado = preco - (preco * 0.05)
print('O Produto que custava R${} com 5% de desconto custará R${:.2f}'.format(preco,resultado))