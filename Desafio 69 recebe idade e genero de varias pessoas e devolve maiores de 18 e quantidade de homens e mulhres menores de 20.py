tot18 = totm = totf20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade>=18:
        tot18+=1
    if sexo == 'M':
        totm+=1
    if sexo =='F' and idade<20:
        totf20+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O número total de pessoas com mais de 18 anos foi: {tot18}')
print(f'O total de homens foi: {totm}')
print(f'O total de mulheres abaixo de 18 anos foi: {totf20}\n')