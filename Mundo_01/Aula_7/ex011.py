print('===== DESAFIO 11 =====')
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
a = alt * larg
t = a / 2
print('A área da sua parede é de {:.2f} m².'
      '\nSerão necessários {:.2f} litros de tinta.'.format(a, t))
