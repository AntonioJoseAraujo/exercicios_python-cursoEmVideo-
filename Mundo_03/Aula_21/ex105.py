print('===== DESAFIO 105 =====')
"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)
Adicione também as docstrings da função
"""

# def notas(*n, sit=False):
#     '''
#     -> Função para analisar notas e situações de vário alunos.
#     :param n: Uma ou mais notas de aluno (aceita várias).
#     :param sit: Valor opcional, indicando se deve ou não colocar a situação.
#     :return: Dicionário com várias informações sobre a situação da turma.
#     '''
#     tot = sum(n)
#     dado = dict()
#     dado["total"] = len(n)
#     dado["maior"] = max(n)
#     dado["menor"] = min(n)
#
#     dado["média"] = tot / dado["total"]
#     if sit:
#         if dado["média"] < 5:
#             dado["situação"] = 'RUIM'
#         elif dado["média"] >= 7:
#             dado["situação"] = 'BOA'
#         elif dado["média"] >= 5:
#             dado["situação"] = 'RAZOÁVEL'
#
#     return dado
#
#
# # Programa Principal
# resp = notas(5, 5.5, 8.5, 9, sit=True)
# print(resp)

print('\n *** Resposta do Professor esta comentado ***')


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vário alunos.
    :param n: Uma ou mais notas de aluno (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não colocar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 10, 7.5, sit=True)
print(resp)
help(notas)
