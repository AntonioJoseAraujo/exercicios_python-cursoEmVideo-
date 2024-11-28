from Mundo_03.MeuMenu.MenuChaveiro.interface import *
from Mundo_03.MeuMenu.MenuChaveiro.arquivo import *
from Mundo_03.MeuMenu.MenuChaveiro.calculos import *
from time import sleep

arq_prod = 'arquivo_de_produtos.txt'
arq_clt = 'arquivo_de_cliente.txt'

if not arquivoExiste(arq_prod):  # Verifica se ja existe o arquivo, se não vai para o criar
    criarArquivo(arq_prod)  # Cria o arquivo

if not arquivoExiste(arq_clt):
    criarArquivo(arq_clt)

while True:
    resp = menu(['Ver Produtos', 'Cadastrar Produtos', 'Ver Clientes', 'Novo Cliente', 'Saida de Produtos',
                 'Entrada de Produtos', 'Sair do Sistema'])
    if resp == 1:
        cabecalho('Ver Produtos')
        lerArquivo(arq_prod)
    elif resp == 2:
        cabecalho('Cadastrar Produtos')
        tipo = str(input('Tipo: '))
        modelo = str(input('Modelo: '))
        qtd = leiaInt('Quantidade: ')
        cadastroProd(arq_prod, tipo, modelo, qtd)
    elif resp == 3:
        cabecalho('Ver Cliente')
        lerArquivo(arq_clt)
    elif resp == 4:
        cabecalho('Novo Cliente')
        nome = str(input('Nome: '))
        end = str(input('Endereço: '))
        fone = leiaInt('Telefone: ')
        cadastroClt(arq_clt, nome, end, fone)
    elif resp == 5:
        cabecalho('Saida de Produtos')
        tipo = str(input('Tipo: '))
        modelo = str(input('Modelo: '))
        qtd_s = leiaInt('Quantidade de Saida: ')
        saidaProd(arq_prod, tipo, modelo, qtd_s)
    elif resp == 6:
        cabecalho('Entrada de produtos')
        tipo = str(input('Tipo: '))
        modelo = str(input('Modelo: '))
        qtd_e = leiaInt('Quantidade de Entrada: ')
        entradaProd(arq_prod, tipo, modelo, qtd_e)
    elif resp == 7:
        print('\033[33mSaindo do Sistema... Até logo!\033[m')
        sleep(2)
        break
    else:
        print(f'\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
