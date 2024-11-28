print('===== DESAFIO 25 =====')
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = input('Digite seu nome: ')
print(nome.find('Silva'))


# -----------------------------------------------------------
nome = str(input('Digite seu nome completo: ')).strip()
temSilva = 'SILVA' in nome.upper()

print('Seu nome tem Silva? {}'.format(temSilva))