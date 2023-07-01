def area(a,b):
    resultado = a * b
    print(f'A área do terreno {L}x{A} é de {resultado:.1f}m²')


L = float(input('Largura (m): '))
A = float(input('Comprimento (m): '))
area(L,A)