print('===== DESAFIO 42 =====')
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais / Isósceles: dois lados iguais / Escaleno: todos os lados diferentes

r1 = float(input('Valor da 1ª reta: '))
r2 = float(input('Valor da 2ª reta: '))
r3 = float(input('Valor da 3ª reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo com esses comprimentos.')
    if r1 == r2 and r2 == r3:
        print('É possível fazer um triangulo Equilátero.')
    elif r1 != r2 or r2 != r3:
        print('É possível fazer um triangulo Escaleno.')
    elif r1 == r2 or r1 == r3:
        print('É possível fazer um triangulo Isósceles.')
else:
    print('Não é possível formar um triangulo.')

print('\n----- Resolução do Professor esta comentada -----')

# r1 = float(input('Valor da 1ª reta: '))
# r2 = float(input('Valor da 2ª reta: '))
# r3 = float(input('Valor da 3ª reta: '))
#
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('É possível formar um triangulo com esses comprimentos.')
#     if r1 == r2 == r3:
#         print('É possível fazer um triangulo Equilátero.')
#     elif r1 != r2 != r3 != r1:
#         print('É possível fazer um triangulo Escaleno.')
#     else:
#         print('É possível fazer um triangulo Isósceles.')
# else:
#     print('Não é possível formar um triangulo.')
