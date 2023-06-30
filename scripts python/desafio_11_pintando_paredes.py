l = float(input('Largura da Parede:'))
a = float(input('Altura da Parede:'))
area = l * a
print('A parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l,a,area))
tinta = area / 2
print('Para pintar essa parede, será necessário {}l de tinta'.format(tinta))