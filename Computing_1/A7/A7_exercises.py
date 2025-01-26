# Importação de módulos
from random import randint

# Para exercício 2:
import sys
sys.path.append("D:\\Reposotories\\UFRJ\\Computing_1")
# Aqui foi necessário usar o sys porque a função está em outra pasta, e sem ser subpasta de A6
from A5.A5_exercises import cadastra_contato

# 1 - Dados iguais
def dados_iguais():
    '''Retorna quatas jogadas foram necessárias para que dois dados caissem com a mesma face para cima.
    Entrada:    vazia           Retorno:    número de jogadas'''

    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    jogadas = 1

    while dado_1 != dado_2:
        dado_1 = randint(1,6)
        dado_2 = randint(1,6)
        jogadas += jogadas
    
    return jogadas

#Testes
# print(dados_iguais())
# print(dados_iguais())
# print(dados_iguais())










# 2 - Contatinhos App
# Função auxiliar para criar a lista de contatos:

agenda = []   # Variável global

def contatos(contato):
    '''Adiciona uma pessoa a lista de contatos do aplicativo.
    Entrada: lista com as informações de um contato         Retorno: lista com todos os contatos'''
    
    list.append(agenda,contato)

    return agenda

# Criando pessoas:
vitor = cadastra_contato('Vitor Abreu', '21900000000', 'vitor@gmail.com', 'vitor@insta')
paulo = cadastra_contato('PAULO VITOR', '21911111111', 'pv@gmail.com', 'pv@insta')
amanda = cadastra_contato('Amanda abreu', '21922222222', 'amanda@gmail.com', 'amanda@insta')
gabriela = cadastra_contato('Gabriela Silva', '21933333333', 'gabi@gmail.com', 'gabi@insta')
lucas = cadastra_contato('Lucas', '21944444444', 'lucas@gmail.com', 'lucas@insta')
joao = cadastra_contato('João Gabriel', '21955555555', 'jg@gmail.com', 'jg@insta')
bianca = cadastra_contato('Bianca Vitor Abreu', '21966666666', 'bva@gmail.com', 'bva@insta')

# Cadastrando pessoas na agenda:

contatos(vitor)
contatos(paulo)
contatos(amanda)
contatos(gabriela)
contatos(lucas)
contatos(joao)
contatos(bianca)
# print(agenda)


# Agora sim, função de fato pedida no exercício
def busca_contatinho(agenda, nome):
    '''Busca as informações de contatos com o nome buscado.
    Entrada: lista de contatos          Retorna: lista com os contatos que possuem o nome pesquisado'''

    # Correções de entrada
    nome1 = str.upper(nome[0]) + nome[1:]   # Opção: Aaaaaaa    corrigindo aaaaaaa
    nome2 = nome[0] + str.lower(nome[1:])   # Opção: Aaaaaaa    corrigindo AAAAAAA
    nome_caixabaixa = str.lower(nome)       # Opção: aaaaaaa
    nome_caixaalta = str.upper(nome)        # Opção: AAAAAAA

    buscador = 0
    tamanho_agenda = len(agenda)
    resultados = []

    while buscador < tamanho_agenda:
        if (nome1 in agenda[buscador][0]) or (nome2 in agenda[buscador][0]) or (nome_caixabaixa in agenda[buscador][0]) or (nome_caixaalta in agenda[buscador][0]):
            resultados = resultados + [agenda[buscador]]

        buscador += 1
    
    return resultados

#Testes
# print(busca_contatinho(agenda, 'Amanda'))
# print(busca_contatinho(agenda, 'vitor'))
# print(busca_contatinho(agenda, 'ABREU'))
# print(busca_contatinho(agenda, 'gabriel'))
# print(busca_contatinho(agenda, 'gabriela'))