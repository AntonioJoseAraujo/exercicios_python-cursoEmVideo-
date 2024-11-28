print('===== DESAFIO 06 =====')
n = int(input('Digite um número: '))

print('Você escolheu o número {};'
      '\nO dobro deste valor é {};'
      '\nO triplo deste valor é {};'
      '\nA raiz quadrada deste valor é {:.2f}.'.format(n, (n*2), (n*3), pow(n, 1/2)))
