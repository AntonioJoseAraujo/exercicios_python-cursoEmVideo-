print('===== DESAFIO 55 =====')
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# muita dificuldade estutar mais as condições

# maior_peso = 0
# menor_peso = 0

# for c in range(1, 6):
#     peso = float(input('Qual é o peso? (Kl) '))
#     if c == 1:
#         maior_peso = peso
#         menor_peso = peso
#
#     elif peso > maior_peso:
#         maior_peso = peso
#
#     elif peso < menor_peso:
#         menor_peso = peso
#
# print('''MAIOR {}
# MENOR {}'''.format(maior_peso, menor_peso))

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
