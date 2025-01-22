# 1 - Série de exercícios de Contatinhos App
# (a) Funcionalidade de cadastro de contatos
def cadastra_contato(nome, telefone = '', email = '', instagram = ''):
    '''Cadastra um novo usuário no aplicativo.
    Informe: (nome, telefone, email, instagram)
    
    Identificação de tipos trabalhados na função
    Entradas: (str, list, str, str)
    Saída: list'''

    novo_contato = [nome, [telefone], email, instagram]
    return novo_contato

#Testes
# print(cadastra_contato('Vitor', '21912345678', 'abcd@gmail.com', 'vitor@abcd'))
# print(cadastra_contato('Vitor'))

# (b) Funcionalidade de atualização de cadastro
def atualiza_cadastro(infos ,indice ,novo_dado):
    '''Atualiza as informações cadastrais de uma pessoa registrada em contatinhos App.
    Informe: (informações do contato numa lista, indice da mudança seguindo a tabela da descrição, informação nova)
    
    Tabela:
    0 | nome
    1 | telefone
    2 | email
    3 | instagram
    
    Identificação de tipos trabalhados na função
    Entradas: (list, int, str)
    Saída: bool'''

    if indice == 0:
        infos[0] = novo_dado
        modificacao = True
    if indice == 1:
        if novo_dado in infos[1]:
            modificacao = False
        else:
            if '' in infos[1]:
                infos[1][0] = novo_dado
                modificacao = True
            else:
                infos[1] += [novo_dado]
                modificacao = True
    if  indice == 2:
        infos[2] = novo_dado
        modificacao = True
    if  indice == 3:
        infos[3] = novo_dado
        modificacao = True
    else:
        modificacao = False
    
    return modificacao

#Testes
#Criando listas de usuários para testes
vitor = cadastra_contato('Vitor', '21912345678', 'abcd@gmail.com', 'vitor@abcd')
fulano = cadastra_contato('fulaninho')

#Modificando dados de usuário
# print(vitor)                                                # Antes
# print(atualiza_cadastro(vitor, 0, 'Abreu'))
# print(vitor)                                                # Modificação 1
# print(atualiza_cadastro(vitor, 1, '21912345678'))
# print(vitor)                                                # Modificação 2 (Não modifica porque já tem esse telefone)
# print(atualiza_cadastro(vitor, 1, '21998765432'))
# print(vitor)                                                # Modificação 3
# print(atualiza_cadastro(vitor, 2, 'vitor@gmail.com'))
# print(vitor)                                                # Modificação 4
# print(atualiza_cadastro(vitor, 3, 'vitor_insta'))
# print(vitor)                                                # Modificação 5
# print(atualiza_cadastro(vitor, 4, ''))                      # Não modifica

#Testando inclusão de informações em fulano
# print(fulano)
# print(atualiza_cadastro(fulano, 0, 'Fulano'))
# print(fulano)
# print(atualiza_cadastro(fulano, 1, ''))
# print(fulano)
# print(atualiza_cadastro(fulano, 1, '21912345678'))
# print(fulano)
# print(atualiza_cadastro(fulano, 2, 'fulano@gmail.com'))
# print(fulano)
# print(atualiza_cadastro(fulano, 3, 'fu_insta'))
# print(fulano)
# print(atualiza_cadastro(fulano, 4, ' '))


# 2 - Cadeia de Aminoácidos que sintetizaram uma proteína
def traduz_RNA(molecula_rna):
    '''Retorna os três aminoácidos correspondentes a uma molécula de RNA responsáveis por sintetizar uma proteína.
    Informe: (molecula_rna) a sequência de 3 trincas que representam a molécula de RNA mensageiro
    
    Identificação de tipos trabalhados na função
    Entradas: str
    Saída: str'''

    trinca_1 = molecula_rna[:3]
    trinca_2 = molecula_rna[3:6]
    trinca_3 = molecula_rna[6:]

    tradutor = {'UUU':'Phe', 'CUU':'Leu', 'UUA':'Leu', 'AAG':'Lisina', 'UCU':'Ser', 'UAU':'Tyr', 'CAA':'Gln'}
    aminoacidos = tradutor[trinca_1] + '-' + tradutor[trinca_2] + '-' + tradutor[trinca_3]

    return aminoacidos

#Testes
# print(traduz_RNA('UUUUUAUCU'))
# print(traduz_RNA('UUUCUUUUA'))
# print(traduz_RNA('UUUAAGUCU'))
# print(traduz_RNA('UAUCAAUUA'))
# print(traduz_RNA('UUACUUUUA'))