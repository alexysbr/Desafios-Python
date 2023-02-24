print()
num = (int(input('Digite 1° número: ')),
       int(input('Digite 2° número: ')),
       int(input('Digite 3° número: ')),
       int(input('Digite 4° número: ')))
print(f'Os números digitados foram: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}.') #index da erro se o valor nao estiver na tupla
else:
    print('O número 3 não foi digitado.')
print('Os números pares são: ', end='')
for n in num:
    if n%2 == 0:
        print(n, end=' ')
print('\n')