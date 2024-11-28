from Mundo_03.Aula_23.ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # rt - le o arquivo, se ja existe
        a.close()
    except FileNotFoundError:  # qualquer outro erro que posso ter do arquivo não existir
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # wt+ - cria um arquivo txt com o nome que foi passado
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')  # Se tiver qualquer erro na criação vai aparecer essa msg
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        # print(a.read())  # vai ler todo o arquivo, assim ficou feio
        for linha in a:
            dado = linha.strip(';')  # Remove ;
            dado[1].replace('\n', '')  # Troca o \n por ''(vazio) nada, ja que ele pula de linha quando cadastra
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # Adiciona as informações
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
