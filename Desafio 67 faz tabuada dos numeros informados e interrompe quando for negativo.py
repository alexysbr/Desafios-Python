while True:
    n = int(input('Informe um número para calcular a tabuada: '))
    if n<0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('#'*30+'\n')
print('ENCERRADO PELO USUÁRIO\n')
