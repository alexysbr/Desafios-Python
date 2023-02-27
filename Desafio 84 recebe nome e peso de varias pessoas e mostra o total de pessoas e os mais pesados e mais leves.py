temp = []
princ = []
mai = men = 0
print()
while True:
    temp.append(str(input('Informe o nome: ')))
    temp.append(float(input('Informe o peso: ')))
    if len(princ) == 0:
        main = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Foram cadastrados {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} kg. Que correspode: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men} kg. Que correspode: ',end='')
for p in princ:
    if p[1]==men:
        print(f'[{p[0]}] ', end='')
print('\n')