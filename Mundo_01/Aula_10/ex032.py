print('===== DESAFIO 32 =====')
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite um ano para saber se ele foi Bissexto: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é Bissexto.'.format(ano))
else:
    print('Esse ano {} não foi Bissexto.'.format(ano))

print('\n----- Resolução do Professor esta comentada -----')
# from datetime import date
# ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
# if ano == 0:
#     ano = date.today().year # importa a data atual e o year somente o ano
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} é BISSEXTO'.format(ano))
# else:
#     print('O ano {} NÃO é BISSEXTO'.format(ano))
