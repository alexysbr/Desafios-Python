'''à vista dinheiro/cheque 10% de desconto
à vista no cartão 5% de desconto
em até 2x no cartão preço normal
em 3x ou mais no cartão 20% de juros'''

preco = float(input('\nInforme o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] em 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Informe a opção desejada: '))
if opcao == 1:
    total = preco - (preco*0.1)
elif opcao == 2:
    total = preco - (preco*0.05)
elif opcao == 3:
    total = preco
    parcela = total/2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros')
elif opcao == 4:
    total = preco+(preco*0.2)
    totparc = int(input('Quantas parcelas? '))
    parcela = total/totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.\n')
