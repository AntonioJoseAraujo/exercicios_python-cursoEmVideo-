print('===== DESAFIO 115a =====')
'''Vamos criar um menu em Python, usando modularização.
1 - Ver pessoas cadastradas
2 - Cadastrar nova Pessoa
3 - Sair do Sistema'''
from Mundo_03.Aula_23.ex115.lib.interface import *

from Mundo_03.Aula_23.ex115.lib.arquivo import *

from time import sleep

arq = 'cursoemvideo.txt'  # Nome do arquivo
if not arquivoExiste(arq):  # Verifica se ja existe o arquivo, se não vai para o criar
    criarArquivo(arq)  # Cria o arquivo

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
