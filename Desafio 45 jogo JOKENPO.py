from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''\nEscolha entre:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qua é a sua jogada? '))
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print(f'\nComputador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}\n')
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!\n')
    elif jogador == 1:
        print('Jogador VENCEU!\n')
    elif jogador == 2:
        print('O computador VENCEU!\n')
    else:
        print('Jogada inválida!\n')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('O computador VENCEU!\n')
    elif jogador == 1:
        print('EMPATE!\n')
    elif jogador == 2:
        print('Jogador VENCEU!\n')
    else:
        print('Jogada inválida!\n')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador VENCEU!\n')
    elif jogador == 1:
        print('O computador VENCEU!\n')
    elif jogador == 2:
        print('EMPATE!\n')
    else:
        print('Jogada inválida!\n')