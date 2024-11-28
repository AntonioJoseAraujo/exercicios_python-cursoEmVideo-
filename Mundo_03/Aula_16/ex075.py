print('===== DESAFIO 75 =====')
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# num1 = int(input('Digite um valor: '))
# num2 = int(input('Digite outro valor: '))
# num3 = int(input('Digite mais um valor: '))
# num4 = int(input('Digite o último valor: '))
#
# valores = (num1, num2, num3, num4)
# print(f'Você digitou os valores: {valores}')
# print(f'O valor 9 apareceu {valores.count(9)} vezes')
# if valores.count(3) == 0:
#     print(f'O valor 3 não foi digitado em nenhuma posição')
# else:
#     print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
# par1 = par2 = par3 = par4 = 0
# if num1 % 2 == 0:
#     par1 = num1
# elif num2 % 2 == 0:
#     par2 = num2
# elif num3 % 2 == 0:
#     par3 = num3
# elif num4 % 2 == 0:
#     par4 = num4
#
# pares = (par1, par2, par3, par4)
# # Preciso tirar os 0 que aparece caso não seja digitado (não consegui)
# print(f'Os valores pares digitados foram {pares}')

print('\n *** Resposta do Professor esta comentado ***')

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count((9))} vezes ')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
