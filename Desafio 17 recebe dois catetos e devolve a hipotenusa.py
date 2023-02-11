'''catetoa = float(input('Digite o valor do cateto adjacente: '))
catetoo = float(input('Digite o valor do cateto oposto: '))
print(f'O valor da hipotenusa é: {(catetoa**2 + catetoo**2)**(1/2)}')'''

# Metódo resolvido nos comentários do vídeo, a diferença é o resultado com duas casas decimais
catetoa = float(input('Digite o valor do cateto adjacente: '))
catetoo = float(input('Digite o valor do cateto oposto: '))
hipot = (catetoa**2 + catetoo**2)**(1/2)
print(f'O valor da hipotenusa é: {hipot:.2f}')