print('===== DESAFIO 31 =====')
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.5
# por Km para viagens até 200km e R$0.45 para viagens mais longas.

distancia = float(input('Qual a distância de sua viagem em KM: '))
passagem = distancia * 0.5
passagem_longas = distancia * 0.45

if distancia <= 200:
    print('Sua viagem é curta, o valor de sua passagem é de R${:.2f}'.format(passagem))
else:
    print('Sua viagem é longa, o valor da passagem é de R${:.2f}'.format(passagem_longas))

print('\n *Coloquei muitas variáveis tentar diminiur ')
print('\n----- Resolução do Professor esta comentada -----')

# distancia = float(input('Qual é a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preco))
