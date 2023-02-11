r1 = float(input('\nPrimeira reta: '))
r2 = float(input('Segunta reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nPODE FORMAR UM TRIÂNGULO!\n')
else:
    print('\nNÃO PODE FORMAR UM TRIÂNGULO!\n')