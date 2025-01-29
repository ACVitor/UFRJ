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