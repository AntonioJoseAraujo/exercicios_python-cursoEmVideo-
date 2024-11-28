from random import randint
from time import sleep

dado01 = randint(0, 5)
cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'branco': '\033[7;40m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;42m'}
print('-=-' * 20)
print('{}Tente Adivinhar o número de 0 a 5 {}'.format(cores['verde'], cores['limpa']))
print('-=-' * 20)
num = int(input('Qual é o seu chute? '))
print('-=-' * 20)
print('{}VERIFICANDO...{}'.format(cores['branco'], cores['limpa']))
print('-=-' * 20)
sleep(3)
if num == dado01:
    print('{}PARABÉNS VOCÊ VENCEU!!!{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}VOCÊ PERDEU!!! O número correto era {}{}'.format(cores['vermelho'], dado01, cores['limpa']))
