print('===== DESAFIO 81 =====')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# lista = []
# while True:
#     num = int(input('Digite um valor: '))
#     lista.append(num)
#
#     op = ' '
#     while op not in 'SN':
#         op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
#     if op == 'N':
#         break
# print(f'Essa lista tem {len(lista)} valores.')
# lista.sort(reverse=True)
# print(f'Essa é a lista em ordem decrescente {lista}')
# if 5 in lista:
#     print(f'O número 5 consta na lista {lista}')
# else:
#     print(f'O número 5 NÃO consta na lista {lista}')

print('\n *** Resposta do Professor esta comentado ***')

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte de lista!')
else:
    print('O valor 5 não faz parte da lista!')
