#aproveitando codigo do desafio 35

r1 = float(input('\nPrimeira reta: '))
r2 = float(input('Segunta reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nPODE FORMAR UM TRIÂNGULO!\n')
    if r1==r2==r3:
        print('É possível formar um triângulo Equilátero!\n')
    elif r1!=r2!=r3!=r1:
        print('É possível formar um triângulo Escaleno!\n')
    else:
        print('É possível formar um triângulo Isósceles!\n')
else:
    print('\nNÃO PODE FORMAR UM TRIÂNGULO!\n')