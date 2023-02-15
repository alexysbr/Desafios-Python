num = int(input('\nDigite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m ', end='')
        tot += 1
    else:
        print('\33[33m ', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é Primo!\n')
else:
    print('E por isso ele Ñ é Primo!\n')