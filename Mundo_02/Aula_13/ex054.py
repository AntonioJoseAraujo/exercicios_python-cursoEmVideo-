print('===== DESAFIO 54 =====')
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    nasc = int(input('Qual é o ano de nascimento da pessoa: '))
    ano = atual - nasc
    if ano >= 20:
        maior += 1
    else:
        menor += 1

print('''{} pessoas são MAIORES de idade.
{} pessoas são MENORES de idade.'''.format(maior, menor))
print('\n*** Resposta do Professor esta comentado ***')

# atual = date.today().year
# totalmaior = 0
# totalmenor = 0
# for pess in range(1, 8):
#     nasc = int(input('Em que ano a {}ª pessoa nasceu? ').format(pess))
#     idade = atual - nasc
#     if idade >= 21:
#         totalmaior += 1
#     else:
#         totalmenor += 1
# print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
# print('E também {} pessoas menores de idade'.format(totalmenor))
