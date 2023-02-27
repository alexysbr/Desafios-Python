num = [[],[]]
valor = 0
print()
for c in range(1,8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor%2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os números Pares são: {num[0]}')
print(f'Os números Ímpares são: {num[1]}\n')