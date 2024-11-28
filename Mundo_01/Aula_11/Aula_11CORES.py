# Adicionando cores
print('Teste')
print('\033[4;31mTeste')
print('\033[1;36;43mTeste\033[m')  # colocar no final os para não ficar estendido a faixa de cor
nome = 'Tony'
print('Olá! Muito prazer em te conhecer,{}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretobranco': '\033[7;30m'
}
print('Olá! Muito prazer em te conhecer,{}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))
