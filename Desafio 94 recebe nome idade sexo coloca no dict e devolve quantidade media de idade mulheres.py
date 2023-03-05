galera = list()
pessoa = dict()
soma = media = 0
print()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
        if pessoa['sexo'] in 'MFmf':
            break
        print(('Erro! Valor inválido!'))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] '))
        if resp in 'SNsn':
            break
        print('Erro! Valor inválido!')
    if resp =='N' or resp =='n':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(' ', end='')
        for k,v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print()