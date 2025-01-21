# Importação de Módulos usados nas funções
from math import *

# 1 - SIGA
def siga(info):
    '''Retorna a uma tupla contendo as informações de nome, nota e situação do aluno em uma disciplina.

    Os intens da tupla de entrada são: (nome, nota_p1, nota_p2, nota_p3)    
    
    Tipos:
    Entrada: tupla(str, float, float, float)
    Retorno: tupla(str, float, str)'''

    nome = info[0]
    media = (info[1] + info[2] + info[3]) / 3

    if media >= 7:
        mensagem = 'aprovado', 'Parabéns!'
    
    elif media >= 5:
        mensagem = 'aprovado',
    else:
        mensagem = 'reprovado',

    return (nome, media) + mensagem

#Testes
# print(siga(('Vitor', 3, 10, 8)))
# print(siga(('Vitor', 5, 6, 4)))
# print(siga(('Vitor', 5, 3, 1)))


# 4 - Zodíaco Chinês
def chi_zodiaco(ano):
    '''Esta função encontra o signo de uma pessoa no zodíaco chinês.
    Inofrme: ano de nascimento

    Entrada: int
    Saída: str '''

    signos = 'Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro'
    identificador = ano % 12

    return signos[identificador]

#Testes
# print(chi_zodiaco(1992))
# print(chi_zodiaco(1993))
# print(chi_zodiaco(1994))
# print(chi_zodiaco(1995))
# print(chi_zodiaco(1996))
# print(chi_zodiaco(1997))
# print(chi_zodiaco(1998))
# print(chi_zodiaco(1999))
# print(chi_zodiaco(2000))
# print(chi_zodiaco(2001))
# print(chi_zodiaco(2002))
# print(chi_zodiaco(2003))


# 3 - Valida telefone
def valida_tel(telefone):
    '''Verifica a validade do formato de um número de telefone segundo a norma Brasileira.
    Informe: telefone
    
    Identificação de tipos trabalhados na função
    Entrada: str
    Saída: tupla'''

    n_digitos = len(telefone)

    if n_digitos == 11 or n_digitos == 10 or n_digitos == 9 or n_digitos == 8:      # Verificando validade do formato
        if n_digitos == 11 or n_digitos == 9:                                       # Identificando se é um celular
            if n_digitos == 11:                                                     # Celular com DDD
                formato_tel = telefone[0:2], telefone[2:]
            else:                                                                   # Celular sem DDD
                formato_tel = '', telefone
        else:                                                                       # Caso do telefone fixo
            if n_digitos == 10:                                                     # Fixo com DDD
                formato_tel = telefone[0:2], telefone[2:]
            else:                                                                   # Fixo sem DDD
                formato_tel = '', telefone
    else:                                                                           # Casos que não são formatos válidos
        formato_tel = '', ''
    
    return formato_tel

#Testes
# print(valida_tel('21912345678'))    #Celular com DDD
# print(valida_tel('912345678'))      #Celular sem DDD
# print(valida_tel('2112345678'))     #Fixo com DDD
# print(valida_tel('12345678'))       #Fixo sem com DDD
# print(valida_tel('1234567'))        #Número inválido


# 4 - Formatos de data aceitáveis
def formata_data(data):
    '''Informa as formatações possíveis para uma certa entrada como data
    Informe: 'xx/xx/xx' neste formato como uma suposta data
    
    Identificação de tipos trabalhados na função
    Entradas: str
    Saída: tupla'''

    # Fomatos possíveis: dd/mm/yy; mm/dd/yy e yy/mm/dd

    bloco_1 = int(data[0:2])
    bloco_2 = int(data[3:5])
    bloco_3 = int(data[6:])

    if (bloco_1 > 31) or (bloco_2 > 31):
        formatos = ()

    else:
        formatos = 'dd/mm/yy', 'mm/dd/yy', 'yy/mm/dd'

    return formatos
    
    
#Testes
print(formata_data('09/09/00'))
print(formata_data('55/05/99'))
