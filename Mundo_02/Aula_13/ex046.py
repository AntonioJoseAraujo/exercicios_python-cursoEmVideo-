print('===== DESAFIO 46 =====')

print('Contagem regressiva para os fogos...')
from time import sleep

for c in range(10, -1, -1):  # colocando o -1 ele vai contar ate o 0
    print(c)
    sleep(1)
print('CABUM!!!')
