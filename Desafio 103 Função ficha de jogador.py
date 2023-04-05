def ficha(jog='<Desconhecido>', gol=0):
    print (f'\nO jogador {jog} fez {gol} gol(s) no campeonato.\n')

#Programa principal
n = str(input("\nDigite o nome do jogador: "))
g = str(input("Digite o número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)