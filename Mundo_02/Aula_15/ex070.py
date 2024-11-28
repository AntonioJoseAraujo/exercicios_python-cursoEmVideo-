print('===== DESAFIO 70 =====')
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


# total = caro = menor_valor = 0
# nome_prod = ''
#
# while True:
#     nome = str(input('Qual o nome do produto: '))
#     preco = float(input('Preço: R$ '))
#     op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#     print('-' * 30)
#     total += preco
#
#     if preco > 1000:
#         caro += 1
#     else:
#         menor_valor = preco
#         nome_prod = nome
#
#     if menor_valor < menor_valor:
#         nome_prod = nome
#
#     if op != 'S' and op != 'N':
#         op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
#
#     if op == 'N':
#         break
#
# print('-' * 30)
# print(f'''Total da compra R${total:.2f}
# Tem {caro} produtos acima de R$1000
# O Produto {nome_prod} é o produto mais barato. Que custou R${menor_valor:.2f}''')
# print(' === FIM DO PROGRAMA ===')

print('\n *** Resposta do Professor esta comentado ***')

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(':-^40'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
