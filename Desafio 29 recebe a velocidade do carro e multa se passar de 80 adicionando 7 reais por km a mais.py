velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa de R$ {multa:.2f}')
print('Tenha um boa viagem! Dirija com segurança!')