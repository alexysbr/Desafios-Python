# se o valor das parcelas/prestações for superior a 30% do salario da pessoa o emprestimo é negado

casa = float(input('\nDigite o valor do imóvel: R$ '))
salario = float(input('Digite o sálario do comprador: R$ '))
anos = int(input('Digite os anos de financiamento: '))
parcela = casa/(anos*12)
minimo = salario*30/100
print(f'\nPara pagar uma casa de R$ {casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R$ {parcela:.2f}')
if parcela <= minimo:
    print('Empréstimo pode ser CONCEDIDO!\n')
else:
    print('Emprestimo NEGADO!\n')
