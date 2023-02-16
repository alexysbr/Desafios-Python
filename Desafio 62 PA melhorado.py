primeiro = int(input('\nPrimeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais!=0:
    total+=mais
    while cont<=total:
        print(f'{termo} => ', end= '')
        termo += razao
        cont+=1
    print('Pausa')
    mais = int(input('Informe a quantidade de termos a mais: '))
print(f'Progressão atualizada com {total} termos mostrados.\n')