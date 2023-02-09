tabuada = int(input('Digite um número inteiro: '))


print(f'A tabuada de {tabuada} é:\n')
for i in range(10):
    print(f'{tabuada} x {i+1} = {tabuada*(i+1)}')
