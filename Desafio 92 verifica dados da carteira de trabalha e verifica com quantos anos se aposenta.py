from datetime import datetime
dados = dict()
print()
dados['Nome'] = str(input('Digite o nome: '))
nasc = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['Ctps'] = int(input('Digite o número da carteira de trabalho: '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o salário: R$ '))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - nasc
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
print()