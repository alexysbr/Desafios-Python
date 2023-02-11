print('\nPreço R$ 0,5 por km até 200 km, acima de 200 km R$ 0,45 por km.')
distancia= float(input('\nQual é a distância da sua viagem? '))
preco = distancia *0.50 if distancia <= 200 else distancia * 0.45
print(f'\nO preço da sua passagem será de R$ {preco:.2f}.\n')