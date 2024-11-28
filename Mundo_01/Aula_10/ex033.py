print('===== DESAFIO 33 =====')
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O Maior é de {}'.format(maior))
print('O Menor é de {}'.format(menor))

print('\n----- Resolução do Professor esta comentada -----')
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
#
# print('O Maior valor é {}'.format(maior))
# print('O Menor valor é {}'.format(menor))
