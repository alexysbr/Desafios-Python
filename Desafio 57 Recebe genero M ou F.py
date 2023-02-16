sexo = str(input('Informe o seu gênero: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, inform seu gênero: ')).strip().upper()[0]
print(f'Gênero {sexo} registrado com sucesso.\n')