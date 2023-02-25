listanum = []
mai = 0
men = 0
print()
for c in range(0,5):
    listanum.append(int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'\nOs números digitados sâo: {listanum}')
print(f'O maior número foi {mai} nas posições: ', end= '')
for i, v in enumerate(listanum):
    if v == mai:
        print( f'{i+1}... ', end='')
print(f'\nO menor número foi {men} nas posições: ', end= '')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i+1}... ', end='')
print('\n')