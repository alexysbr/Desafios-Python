cid = str(input('Em que cidade você nasceu? ')).strip()
print('Verificando se essa cidade começa com "Santo"...')
print(cid[:5].upper() == 'SANTO')