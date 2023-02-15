soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'\nA soma deu {soma} de um total de {cont} números somados.\n')
