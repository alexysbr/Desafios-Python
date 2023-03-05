time = list()
jogador = dict()
partidas = list()
print()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Digite o número de partidas o {jogador["Nome"]} jogou: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'    Digite o número de gols na partida {c+1}: ')))
    jogador ['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] '))
        if resp in 'SNsn':
            break
        print('Erro! Resposta inválida!')
    if resp == 'N' or resp == 'n':
        break
print()
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Visualizar dados de qual jogador? [999 p/ sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Jogador inexistente!')
    else:
        print()
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    => Na partida {i+1}, fez {g} gols.')
print()
