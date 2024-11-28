print('===== DESAFIO 50 =====')
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor').format(c))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

print('\n*** Resposta do Professor foi mais Simples e elaborada ***')

# Feito e funcional
# s = 0
# par = 0
# for c in range(0, 6):
#     num = int(input('Digite um número inteiro: '))
#     if num % 2 == 0:
#         par += num
#     else:
#         s = num - num
#     s = par
# print('A soma dos números pares é de {}'.format(s))
