from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~~'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa principal
print()
contador(1, 10, 1)
contador(10, 0, 2)
print('~~'*20)
ini = int(input('Digite o Início: '))
fim = int(input('Digite o Fim: '))
pas = int(input('Digite o Passo: '))
contador(ini, fim, pas)
print()