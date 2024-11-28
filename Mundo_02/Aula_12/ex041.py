import datetime

print('===== DESAFIO 41 =====')
#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#  categoria, de acordo com a idade:

from datetime import date

nasc = int(input('Qual seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Sua idade é de {} anos.\n'
          'Você esta na categoria Mirim.'.format(idade))
elif idade <= 14:
    print('Sua idade é de {} anos.\n'
          'Você esta na categoria Infantil.'.format(idade))
elif idade <= 19:
    print('Sua idade é de {} anos.\n'
          'Você esta na categoria Junior.'.format(idade))
elif idade <= 25:
    print('Sua idade é de {} anos.\n'
          'Você esta na categoria Sênior.'.format(idade))
else:
    print('Sua idade é de {} anos.\n'
          'Você esta na categoria Master.'.format(idade))
