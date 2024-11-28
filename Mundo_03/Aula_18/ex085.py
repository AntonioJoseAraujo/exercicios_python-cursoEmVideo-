print('===== DESAFIO 85 =====')
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# lista = [[], []]
#
# for n in range(0, 7):
#     num = (int(input(f'Digite o {n + 1}º valor: ')))
#     if num % 2 == 0:
#         lista[0].append(num)
#     else:
#         lista[1].append(num)
#
# print('=-' * 30)
# print(f'Os valores pares digitados foram: {sorted(lista[0])}')
# print(f'Os valores ímpares digitado foram: {sorted(lista[1])}')

print('\n *** Resposta do Professor esta comentado ***')

núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
