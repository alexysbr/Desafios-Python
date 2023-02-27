num =list()
pares = list()
impares = list()
print()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v%2==0:
        pares.append(v)
    elif v%2 == 1:
        impares.append(v)
print(f'A lista completa é: {num}.')
print(f'A lista de PARES é: {pares}')
print(f'A lista de ÍMPARES é: {impares}.\n')