print('===== DESAFIO 29 =====')
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.

velocidade = float(input('Qual é a velocidade do carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado!\n'
          'O valor da sua multa é de {}'.format(multa))
else:
    print('Parabéns você esta no limite de velocidade.')
print('\n----- Resolução do Professor esta comentada -----')
# velocidade = float(input('Qual a velocidade atual do carro? '))
# if velocidade > 80:
#     print('MULTADO! Você excedeu o limite permitido de 80Km/h')
#     multa = (velocidade - 80) * 7
#     print('Você deve pagar uma multa de R${:.2f}'.format(multa))
# print('Tenha um bom dia! Dirija com segurança!')
