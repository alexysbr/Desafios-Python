numeros = list()
print()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Os números adicionados em ordem crescente são: {numeros}\n')