print('===== DESAFIO 65 =====')
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.


num = maior = menor = soma = int(input('Digite um valor inteiro: '))
op = str(input('Deseja continuar? [S/N] ')).upper().strip()
cont = 1
media = 0

while op == 'S':
    num = int(input('Digite outro valor inteiro: '))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
    soma += num
    media = soma / cont
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()

print('''A média de todos os valores informados foi de {}
O maior número informado foi {}
O menor número informado foi {}
'''.format(media, maior, menor))

print('\n *** Resposta do Professor esta comentado ***')

# resp = 'S'
# soma = quant = media = maior = menor = 0
# while resp in 'Ss':
#     num = int(input('Digite um número: '))
#     soma += num
#     quant += 1
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
#     resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
# media = soma / quant
# print('Você digitou {} números e a média foi {}.'.format(quant, media))
# print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
