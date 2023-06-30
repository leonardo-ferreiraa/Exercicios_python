n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c != 0:
        print('\033[0:m', end='')
    else:
        tot += 1
        print('\033[0:31m', end='')
    print('{} '.format(c), end='')
print('\n\033[0:mO número {} foi divisivel {} vezes'.format(c, tot))
if tot > 2:
    print('O número não é primo!')
else:
    print(('O número é primo!'))