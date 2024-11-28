# def leiaDinheiro(txt):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(txt)).replace(',', '.')
#         if n.replace('.', '', 1).isdigit():
#             valor = float(n)
#             ok = True
#         else:
#             print(f'\033[1;31mERRO! "{n}" Digite um número válido.\033[m')
#             # O número de (n) vai aparece como virgula (,)
#             # print(f'\033[1;31mERRO! "{n.replace('.', ',')}" Digite um número válido.\033[m')
#         if ok:
#             break
#     return valor


# RESPOSTA DO PROFESSOR ficou muito melhor desenvolvida *********
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            válido = True
            return float(entrada)
