print('===== DESAFIO 44 =====')
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento: à vista dinheiro/cheque: 10% de desconto // à vista no cartão: 5% de desconto // até 2x no cartão preço
# normal // 3x ou mais no cartão: 20% de juros

produto = float(input('Qual é o valor do produto R$: '))
pgto = int(input('Informe a forma de pagamento que você deseja.\n'
                 '[1] Dinheiro/Pix: Desconto de 10%\n'
                 '[2] Cartão debito: Desconto de 5%\n'
                 '[3] Cartão até 2x: Sem juros\n'
                 '[4] Cartão 3x ou mais: 20% de juros\n'
                 'Qual sua forma de pagamento: '))

if pgto == 1:
    print('Você vai receber um desconto de 10% no produto.\n'
          'O valor atualizado com desconto é de R$ {:.2f}'.format(produto * 0.9))
elif pgto == 2:
    print('Você vai receber um desconto de 5% no produto.\n'
          'O valor atualizado com desconto é de R$ {:.2f}'.format(produto * 0.95))
elif pgto == 3:
    print('Você vai parcelar em 2x no cartão\n'
          'O valor das parcelas serão de R$ {:.2f}'.format(produto / 2))
elif pgto == 4:
    produto_juros = produto * 1.2
    print('Você vai parcelar em 3x ou mais\n'
          'Nessa forma de pagamento vai ter um juros de 20%')
    parc = int(input('Informe quantas vezes vai parcelar: '))
    if parc < 3:
        print('Valor invalido!')
    else:
        print('O valor atualizado do produto é de R${}\n'
              'As parcelas do produto do produto será de {}x R${}'.format(produto_juros, parc, produto_juros / parc))
else:
    print('Opção Invalida!')

print('\n----- Resolução do Professor esta comentada -----')

# print('{:=^40}'.format(' LOJA do TONY '))
# preço = float(input('Preço das compras: R$'))
# print('''FORMAS DE PAGAMENTO
# [ 1 ] à vista dinheiro/ Pix
# [ 2 ] à vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão''')
# opção = int(input('Qual é a opção'))
# if opção == 1:
#     total = preço - (preço * 10 / 100)
# elif opção == 2:
#     total = preço - (preço * 5 / 100)
# elif opção == 3:
#     total = preço
#     parcela = total / 2
#     print('Sua compra será parcelado em 2x de R${:.2f}'.format(parcela))
# elif opção == 4:
#     total = preço + (preço * 20 / 100)
#     totparc = int(input('Quantas parcelas? '))
#     parcela = total / totparc
#     print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
# else:
#     total = preço
#     print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
# print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
