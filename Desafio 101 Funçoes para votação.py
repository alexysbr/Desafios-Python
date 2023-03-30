def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'\nCom {idade} anos: NÃO VOTA.\n'
    elif 16 <= idade < 18 or idade > 65:
        return f'\nCom {idade} anos: O VOTO É OPCIONAL.\n'
    else:
        return f'\nCom {idade} anos: O VOTO É OBRIGATÓRIO.\n'
    
# Programa principal
nasc = int(input("\nDigite o ano de nascimento: "))
print(voto(nasc))