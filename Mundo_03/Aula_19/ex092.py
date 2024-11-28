print('===== DESAFIO 92 =====')
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Obs.: aposentadoria em 35 anos de contribuição.

# from datetime import datetime
#
# dado = {}
#
# dado['nome'] = str(input('Nome: '))
# ano_nasc = int(input('Ano de Nascimento: '))
# dado['idade'] = datetime.now().year - ano_nasc
# dado['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
#
# if dado['ctps'] == 0:
#     print('-=' * 30)
#     for p, v in dado.items():
#         print(f'{p} tem o valor {v}')
# else:
#     dado['contratação'] = int(input('Ano de contratação: '))
#     dado['salário'] = float(input('Salário: R$ '))
#     dado['aposentadoria'] = (dado['contratação'] + 35) - ano_nasc
#     print('-=' * 30)
#     for p, v in dado.items():
#         print(f'{p} tem o valor {v}')

print('\n *** Resposta do Professor esta comentado ***')
# resposta estava quase igual somente o if estava diferente
from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for p, v in dados.items():
    print(f'{p} tem o valor {v}')
