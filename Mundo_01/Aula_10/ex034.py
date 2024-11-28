print('===== DESAFIO 34 =====')
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Digite o valor do seu salário R$: '))

if salario >= 1250.0:
    novo_salario = salario + (salario * 0.10)
    print('Você tera um aumento de 10%.')
else:
    novo_salario = salario + (salario * 0.15)
    print('Você tera um aumento de 15%.')

print('Seu novo salário é de R${}'.format(novo_salario))

print('\n----- Resolução do Professor esta comentada -----')
# salario = float(input('Qual é o salário do funcionário? R$'))
# if salario <= 1250:
#     novo = salario + (salario * 15 / 100)
# else:
#     novo = salario + (salario * 10 / 100)
# print('Quem ganhava R${:.2f} passa a ganha R${:.2f} agora.'.format(salario, novo))
