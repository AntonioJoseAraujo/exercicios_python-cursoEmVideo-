print('===== DESAFIO 43 =====')
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status.
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso? (Kg) '))
altura = float(input('Digite sua altura? (m) '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é de {:.1f}\n'
          'Você esta ABAIXO do peso ideal.'.format(imc))
elif imc == 18.5 or imc < 25:
    print('Seu IMC é de {:.1f}\n'
          'Você esta no peso IDEAL.'.format(imc))
elif imc == 25 or imc < 30:
    print('Seu IMC é de {:.1f}\n'
          'Você esta com SOBREPESO.'.format(imc))
elif imc == 30 or imc < 40:
    print('Seu IMC é de {:.1f}\n'
          'Você esta na faixa de OBESIDADE.'.format(imc))
else:
    print('Seu IMC é de {:.1f}\n'
          'Você esta na faixa de OBESIDADE MÓRBIDA.'.format(imc))

print('\n----- Resolução do Professor esta comentada -----')

# peso = float(input('Digite seu peso? (Kg) '))
# altura = float(input('Digite sua altura? (m) '))
#
# imc = peso / (altura ** 2)
#
# if imc < 18.5:
#     print('Seu IMC é de {:.1f}\n'
#           'Você esta ABAIXO do peso ideal.'.format(imc))
# elif 18.5 <= imc < 25:
#     print('Seu IMC é de {:.1f}\n'
#           'Você esta no peso IDEAL.'.format(imc))
# elif 25 <= imc < 30:
#     print('Seu IMC é de {:.1f}\n'
#           'Você esta com SOBREPESO.'.format(imc))
# elif 30 == imc < 40:
#     print('Seu IMC é de {:.1f}\n'
#           'Você esta na faixa de OBESIDADE.'.format(imc))
# elif imc >= 40:
#     print('Seu IMC é de {:.1f}\n'
#           'Você esta na faixa de OBESIDADE MÓRBIDA.'.format(imc))
