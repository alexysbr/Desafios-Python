valores = []
print()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram digitados {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os elementos em ordem decrescente são: {valores}')
if 5 in valores:
    print('O número 5 está na lista.\n')
else:
    print('O número 5 NÃO está na lista.\n')