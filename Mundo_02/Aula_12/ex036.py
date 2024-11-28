print('===== DESAFIO 36 =====')
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
emprestimo = int(input('Quantos anos pretende pagar? '))

# calculo do valor da parcela
parcela = (casa / emprestimo) / 12

if parcela <= (salario * 0.30):
    print('Valor da casa {:.2f}\n'
          'Salário do comprador {:.2f}\n'
          'Tempo de pagamento {} anos\n'
          'Valor das parcelas {:.2f} mês\n'
          'Parabéns seu empréstimo foi Autorizado!'.format(casa, salario, emprestimo, parcela))
else:
    print('Valor da casa {:.2f}\n'
          'Salário do comprador {:.2f}\n'
          'Tempo de pagamento {} anos\n'
          'Valor da parcelas {:.2f} mês\n'
          'Seu empréstimo foi Negado.\n'
          'O valor do empréstimo é Superior a 30% do Salário.'.format(casa, salario, emprestimo, parcela))

print('\n----- Resolução do Professor esta comentada -----')
# casa = float(input('Valor da casa: R$:'))
# salario = float(input('Salário do comprador: R$:'))
# anos = int(input('Quantos ano de financiamento? '))
# prestacao = casa / (anos * 12)
# minimo = salario * 30 / 100
# print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
# if prestacao <= minimo:
#       print('Empréstimo pode ser CONCEDIDO!')
# else:
#       print('Empréstimo NEGADO!')
