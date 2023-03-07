def area(larg, comp):
    a = larg*comp
    print(f'A área de um terreno {larg} x {comp} é {a}m² !\n')

# Programa principal
print()
l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))
area(l,c)