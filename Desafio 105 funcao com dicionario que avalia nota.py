def notas(*n, sit=False):
    """
    ->Função para analisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao do aluno
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print()
print(resp)
print()
help(notas)
print()