ficha = list()
print()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('~'*26)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('~'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print()
    opc = int(input('Mostra notas do aluno: (999 para sair) '))
    if opc == 999:
        print('Encerrando...\n')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')