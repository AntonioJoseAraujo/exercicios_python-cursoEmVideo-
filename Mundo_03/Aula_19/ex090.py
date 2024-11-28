print('===== DESAFIO 90 =====')
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

# aluno = {}
# aluno["nome"] = str(input('NOME: '))
# aluno["media"] = float(input(f'Média de {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#     print(f'Nome é igual a {aluno["nome"]}')
#     print(f'Média é igual a {aluno["media"]}')
#     print(f'Situação é igual a APROVADO')
# else:
#     print(f'Nome é igual a {aluno["nome"]}')
#     print(f'Média é igual a {aluno["media"]}')
#     print(f'Situação é igual a REPROVADO')


print('\n *** Resposta do Professor esta comentado ***')

aluno = {}
aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'REPROVADO'

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k}: é igual a {v}')
