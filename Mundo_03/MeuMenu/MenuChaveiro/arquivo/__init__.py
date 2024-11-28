from Mundo_03.MeuMenu.MenuChaveiro.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[32mO {nome} foi criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[31mHouve um ERRO ao ler o arquivo {nome}!\033[m')
    else:
        if nome == 'arquivo_de_produtos.txt':
            cabecalho('\033[36mLista de Produtos\033[m')
            linhas = a.readlines()
            for i in range(0, len(linhas), 3):
                try:
                    tipo = linhas[i].strip()
                    modelo = linhas[i + 1].strip()
                    qtd = linhas[i + 2].strip()
                    print(f'Tipo: {tipo}')
                    print(f'Modelo: {modelo}')
                    print(f'Qtd: {qtd}')
                    print('-' * 50)
                except IndexError:
                    print('\033[31mFormato de linha inválido!\033[m')
        else:
            cabecalho('\033[36mLista de Clientes\033[m')
            linhas = a.readlines()
            for i in range(0, len(linhas), 3):
                try:
                    nome = linhas[i].strip()
                    end = linhas[i + 1].strip()
                    fone = linhas[i + 2].strip()
                    print(f'Nome: {nome}')
                    print(f'Endereço: {end}')
                    print(f'Telefone: {fone}')
                    print('-' * 50)
                except IndexError:
                    print('\033[31mFormato de linha inválido!\033[m')

    finally:
        a.close()


def cadastroClt(arq_clt, nome='desconhecido', end='desconhecido', fone='não informado'):
    try:
        a = open(arq_clt, 'at')
    except:
        print(f'\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};\n{end};\n{fone};\n')
        except:
            print('\033[31mHouve um ERRO ao escrever no arquivo!\033[m')
        else:
            print(f'\033[32mNovo registro {nome} adicionado com sucesso.\033[m')
            a.close()


def cadastroProd(arq_prod, tipo='desconhecido', modelo='desconhecido', qtd=0):
    try:
        a = open(arq_prod, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{tipo};\n{modelo};\n{qtd};\n')
        except:
            print('\033[31mHouve um ERRO ao escrever no arquivo!\033[m')
        else:
            print(f'\033[32mNovo registro Tipo: {tipo}, Modelo: {modelo}, Quantidade: {qtd}.\033[m')
            a.close()
