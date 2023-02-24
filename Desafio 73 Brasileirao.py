'''Tabela do Brasileirao com tupla que informa os primeiros 5 colocados,
os 4 últimos colocados, em ordem alfabética e a posição da Chapecoense'''

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético Mineiro', 'Botafogo', 'Atlético-PR',
         'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print()
print('~~'*15)
print(f'Tabela do Brasileirão: {times}')
print('~~'*15)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('~~'*15)
print(f'Os 4 últimos colocados: {times[-4:]}')
print('~~'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('~~'*15)
print(f'A Chapecoense está na posição: {times.index("Chapecoense")+1}\n')