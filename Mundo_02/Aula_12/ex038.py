print('===== DESAFIO 38 =====')
# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem: O primeiro valor é
# maior // O segundo valor é maior // Não existe valor maior, os dois são iguais
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um outro número: '))
if num1 > num2:
    print('{} é o Maior.'.format(num1))
elif num2 > num1:
    print('{} é o Maior.'.format(num2))
elif num1 == num2:
    print('Não existe valor maior.São iguais.')

print('\n----- Resolução do Professor esta comentada -----')
