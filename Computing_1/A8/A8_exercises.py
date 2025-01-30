# Importações de bibliotecas e funções
from math import pi


# 1 - Quantas vezes um elemento aparece no iterável
def aparicoes(iteravel, elemento):
    '''Conta o número de vezes que um elemento informado aparece dentro de um iterável.
    Entrada: (list or tuple or str, any type)           Retorno: int'''

    repeticoes = 0

    for item in iteravel:
        if item == elemento:
            repeticoes += 1
    
    return repeticoes

#Testes
# print(aparicoes('Vitor','a'))
# print(aparicoes('Ana','a'))
# print(aparicoes((1,2,3,4,5,6,7,8,9,10,1,9,8,7),1))
# print(aparicoes(['a', [1,2,3,4,5], 5, 5.0, '5', (5,1)],5))


# 2 - Quantas vezes um elemento aparece no trecho de um iterável
def aparicoes_trecho(iteravel, elemento, inicio = 0, fim = -1):
    '''Conta o número de vezes que um elemento informado aparece em um trecho de um iterável.
    Entrada: (list or tuple or str, any type, int, int)           Retorno: int'''

    # Corrigindo o tamanho da fatia caso o usuário passe erroneamente
    tamanho = len(iteravel)
    if (abs(inicio) > (tamanho)) and (abs(fim) > tamanho):
        inicio = 0
        fim = -1
    elif (abs(inicio) > (tamanho)):
        inicio = 0
    elif (abs(fim) > tamanho):
        fim = -1
    
    novo_iteravel = iteravel[inicio:fim]
    
    return aparicoes(novo_iteravel,elemento)

#Testes
# print(aparicoes_trecho('Vitor', 'a', -6, 6))
# print(aparicoes_trecho('Vitor', 'V', -6, 6))
# print(aparicoes_trecho('Vitor', 't', -6, -3))
# print(aparicoes_trecho('Vitor', 't', 3, 6))


# 3 - Jogo da forca
def atualiza_mascara(palavra, segredo, letra):
    '''Atualiza o estado atual de uma jogada no jogo forca.
    Entrada: (str, list, str)       Sem retorno'''
    n_letras = range(len(palavra))

    for item in n_letras:
        if palavra[item] == letra:
            segredo[item] = letra

#Testes
# palavra = 'matematica'
# segredo = ['-','-','-','-','-','-','-','-','-','-']
# print(segredo)
# atualiza_mascara(palavra, segredo,'a')
# print(segredo)
# atualiza_mascara(palavra, segredo,'k')
# print(segredo)
# atualiza_mascara(palavra, segredo,'a')
# print(segredo)
# atualiza_mascara(palavra, segredo,'m')
# print(segredo)
# atualiza_mascara(palavra, segredo,'t')
# print(segredo)
# atualiza_mascara(palavra, segredo,'c')
# print(segredo)
# atualiza_mascara(palavra, segredo,'i')
# print(segredo)
# atualiza_mascara(palavra, segredo,'e')
# print(segredo)


# 3 - Exemplo de Série Convergente
#(a) - Soma dos n primeiros termos de an
def serie(n):
    '''Calcula a soma dos n primeiros termos de uma serie de termo geral an.
    Entrada: int        Retorno: float'''

    soma_termos = 0

    for item in range(n):
        soma_termos = soma_termos + ((-1)**item)/(2*item + 1)
    
    return soma_termos

#Testes
# print(serie(2))
# print(serie(5))

#(b) - Número de somas necessárias para que o erro seja menor que 0.01 e valor da soma
def n_somas_necessarias():
    '''Calcula o número de somas necessárias para que o erro seja menor que 0.01 quando comparado ao valor da soma infinita da série do exercício.
    Entrada: não necessário         Return: tuple'''

    contador = 0
    soma = serie(contador)
    erro = abs(soma - pi/4)

    while erro > 0.01:
        contador += 1
        soma = serie(contador)
        erro = abs(soma - pi/4)
    
    return soma, contador

#Testes
print(n_somas_necessarias())