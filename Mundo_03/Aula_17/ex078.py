print('===== DESAFIO 78 =====')
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.


num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-' * 40)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()
print('\n *** Resposta do Professor esta comentado ***')

# listanum = []
# mai = 0
# men = 0
# for c in range(0, 5):
#     listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
#     if c == 0:
#         mai = men = listanum[c]
#     else:
#         if listanum[c] > mai:
#             mai = listanum[c]
#         if listanum[c] < men:
#             men = listanum[c]
#
# print('=-' * 30)
# print(f'Você digitou os valores {listanum}')

# print(f'O maior valor digitado foi {mai} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == mai:
#         print(f'{i}...', end='')

# print(f'O menor valor digitado foi {men} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == men:
#         print(f'{i}...', end='')
# print()
