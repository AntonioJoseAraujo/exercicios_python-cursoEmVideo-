print('===== DESAFIO 17 =====')
# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot 
catO = float(input('Digite a medida do cateto oposto: '))
catA = float(input('Digite a medida do cateto adjacente: '))
hip = hypot(catO, catA)
print('A medida da hipotenusa é {:.2f}.'.format(hip))
