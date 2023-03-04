jogador = dict()
partidas = list()
print()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
tot = int(input(f'Digite o número de partidas o {jogador["Nome"]} jogou: '))
for c in range(0,tot):
    partidas.append(int(input(f'    Digite o número de gols na partida {c+1}: ')))
jogador ['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i,v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.\n')