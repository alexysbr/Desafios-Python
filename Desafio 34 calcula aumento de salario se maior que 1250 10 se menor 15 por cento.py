salario = float(input('\nInforme o salário: R$ '))

if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*0.1)

print(f'\nO salário de R$ {salario:.2f} será reajustado para o salário R$ {novo:.2f}\n')