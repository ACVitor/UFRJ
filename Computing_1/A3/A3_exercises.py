# Importando bibliotecas
from math import *

# Importação de uma função de A2 para o exercício 2 - Informa existência de raízes
import sys
sys.path.append("D:\\Reposotories\\UFRJ\\Computing_1")
# Aqui foi necessário usar o sys porque a função está em outra pasta, e sem subpasta de A3
from A2.A2_exercices import delta


# 1 - Módulo
def modulo(n):
    '''Calcula o módulo de um número
    Entrada: int
    Saída: float '''
    if n >= 0:
        return n
    else:
        return n * (-1)
    
#Testes
# print('Valores da função modulo: ' + str(modulo(5)) + ', ' + str(modulo(-5)) + ', ' + str(modulo(0)) + ', ' + str(modulo(5.2)))
# print('Valores da função abs do módulo math' + ', ' + str(abs(5)) + ', ' + str(abs(-5)) + ', ' + str(0) + ', ' + str(abs(5.2)))

    # Testando com números complexos
# print(modulo(5 + 1j))                                             # Não funciona para complex
# print('Teste da função abs com complex: ' + str(abs(5 + 1j)))     # Funciona para complex


# 2 - Informa existência de raízes
def existe_raiz(a,b,c):
    '''Dados os parâmetros a,b e c de uma eq. do 2°, informa se há raízes reais e a quantidade
    Entrada: int, int, int
    Saída: float'''
    if delta(a,b,c) > 0:
        return 'Existem 2 raízes reais.'
    elif delta(a,b,c) < 0:
        return 'Não existe raíz real.'
    else:
        return 'Existe uma raíz real'
    
#Testes
# print(existe_raiz(1,2,1))   # Delta == 0
# print(existe_raiz(1,4,1))   # Delta > 0
# print(existe_raiz(2,2,1))   # Delta < 0