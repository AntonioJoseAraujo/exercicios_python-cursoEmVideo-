print('===== DESAFIO 82 =====')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.

# lista = []
# listaPares = []
# listaImpares = []
# while True:
#     num = int(input('Digite um número: '))
#     lista.append(num)
#     if num % 2 == 0:
#         listaPares.append(num)
#     if num % 2 == 1:
#         listaImpares.append(num)
#     op = ' '
#     while op not in 'SN':
#         op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
#     if op == 'N':
#         break
# print(f'Lista de todos os números {lista}')
# print(f'Lista de PARES {listaPares}')
# print(f'Lista de IMPARES {listaImpares}')

print('\n *** Resposta do Professor esta comentado ***')

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número:')))
    resp = str(input('Quer continuar ? [S/N '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
