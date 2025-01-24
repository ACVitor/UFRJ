# Importação de bibliotecas

import sys
sys.path.append("D:\\Reposotories\\UFRJ\\Computing_1")
# Aqui foi necessário usar o sys porque a função está em outra pasta, e sem ser subpasta de A6
from A5.A5_exercises import cadastra_contato
from A5.A5_exercises import atualiza_cadastro

# 1 - Exclui telefone
def exclui_tel(infos, telefone = ''):
    '''Exclui o telefone informado da lista de telefones de um contato caso o telefone tenha sido cadastrado anteriormente.
    Informe: (lista contendo as informações do contato, telefone a ser excluído)
    
    Identificação de tipos trabalhados na função
    Entradas: (list, str)
    Saída: bool'''

    if telefone in infos[1]:
        list.remove(infos[1], telefone)
        modificacao = True

    else:
        modificacao = False
    
    return modificacao

#Testes
#Cadastrando contato de teste e adicionando telefone para exercício 1.
# vitor = cadastra_contato('Vitor', '21912345678', 'vitor@gmail.com', 'vitor@insta')
# atualiza_cadastro(vitor,1,'21911111111')
# print(vitor)

# print(exclui_tel(vitor,'21987654321'))
# print(vitor)

# print(exclui_tel(vitor,'21912345678'))
# print(vitor)


# 2 - Campeonato
# Função auxílio para cadastramento de times
def inscricao_campeonato(time,pontos,tabela = {}):
    '''Cadastra novos times à tabela do campeonato
    Informe: (nome do time, pontos feitos pelo time no campeonato)
    
    Identificação de tipos trabalhados na função
    Entradas: (str, int)
    Saída: dict'''

    tabela[time] = pontos

    return tabela

# Função do exercício
def campeonato(tabela):
    '''Retorna a lista dos times participantes do campeonato, a pontuação do time vencedor e a média de pontos do campeonato.
    Informe: A tabela contendo os times e os pontos de cada time.
    
    Identificação de tipos trabalhados na função
    Entradas: (dict)
    Saída: list'''

    participantes = list(dict.keys(tabela))
    numero_participantes = len(participantes)
    pontos = list(dict.values(tabela))
    media_pontos = int(sum(pontos) / numero_participantes)

    #Identificando a pontuação campeã
    list.sort(pontos)
    campeao = pontos[-1]

    infos_campeonato = [participantes, campeao, media_pontos]

    return infos_campeonato

# # Cadastro de times no campeonato
# tabela = {}
# inscricao_campeonato('Fortaleza', 53, tabela)
# inscricao_campeonato('Grêmio', 65, tabela)
# inscricao_campeonato('Corinthians', 56, tabela)
# inscricao_campeonato('Internacional', 57, tabela)
# inscricao_campeonato('Bahia', 49,tabela)
# inscricao_campeonato('Fluminense', 46,tabela)
# inscricao_campeonato('Palmeiras', 74, tabela)
# inscricao_campeonato('Cruzeiro', 36, tabela)
# inscricao_campeonato('Vasco da Gama', 49,tabela)
# inscricao_campeonato('Chapecoense', 32, tabela)
# inscricao_campeonato('São Paulo', 63, tabela)
# inscricao_campeonato('CSA', 32, tabela)
# inscricao_campeonato('Atlético Mineiro', 48,tabela)
# inscricao_campeonato('Botafogo', 43, tabela)
# inscricao_campeonato('Athletico-PR', 64 ,tabela)
# inscricao_campeonato('Goiás', 52, tabela)
# inscricao_campeonato('Ceará', 39, tabela)
# inscricao_campeonato('Avaí', 20, tabela)
# inscricao_campeonato('Flamengo', 90, tabela)
# inscricao_campeonato('Santos',74, tabela)
# # print(tabela)


# # Testes da função
# print(campeonato(tabela))