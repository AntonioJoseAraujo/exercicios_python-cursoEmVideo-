print('=====  DESAFIO 18 =====')
# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = int(input('Digite o valor do ângulo desejado: '))
sn = sin(radians(ang))
cs = cos(radians(ang))
tg = tan(radians(ang))
print('O valor do SENO é {:.2f};\n'
      'O valor do COSSENO é {:.2f};\n'
      'O valor da TANGENTE é {:.2f}.'.format(sn, cs, tg))
