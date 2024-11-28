print('===== DESAFIO 35 =====')
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

r1 = float(input('Digite um comprimento: '))
r2 = float(input('Digite outro comprimento: '))
r3 = float(input('Digite mais um comprimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo com esses comprimentos.')
else:
    print('Não é possível formar um triangulo.')
print('\n----- Resolução do Professor esta comentada -----')
