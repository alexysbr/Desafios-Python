from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'\nOs números sorteados foram: {num}')
print(f'O maior número sorteado foi: {max(num)}')
print(f'O menor número sorteado foi: {min(num)}\n')