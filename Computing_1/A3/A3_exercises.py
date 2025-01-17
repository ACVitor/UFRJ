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


# 3 - Replicagem de texto
def replica_txt(texto, n):
    '''Replica um número n de vezes uma frase.
    Entradas:   texto, n (str, int)
    Saída: str'''
    return (texto + ' ') * n

#Testes
# print(replica_txt('Feliz Aniversário!', 10000))


# 4 - Formata data
def form_data(dd, mm, aa):
    '''Formata os valores de entrada no padrão dd/mm/aa
    Entradas: dd [dia], mm [mês], aa [ano]      (int, int, int)
    Saída: str
    Obs.: Informar nesta ordem para funcionamento correto da função'''

    if dd < 10 or mm < 10:
        if dd < 10 and mm < 10:
            return '0' + str(dd) + '/' + '0' + str(mm) + '/' + str(aa)
        elif dd < 10:
            return '0' + str(dd) + '/' + str(mm) + '/' + str(aa)
        elif mm < 10:
            return str(dd) + '/' + '0' + str(mm) + '/' + str(aa)
    
    else:
        return str(dd) + '/' + str(mm) + '/' + str(aa)

#Testes
# print(form_data(1,10,2000))
# print(form_data(10,7,2000))
# print(form_data(1,7,2000))
# print(form_data(10,10,2000))


# 5 - Comportamento da função do exercício
def f_partes_exercicio(x):
    '''Calcula o valor de f(x), função por partes definida no exercício 5 da lista
    Entradas: x (float)
    Saída: str'''

    if x < 0:
        return 'Para x = ' + str(x) + ', f(x) = ' + str(0)
    elif x >= 0 and x <= 2:
        return 'Para x = ' + str(x) + ', f(x) = ' + str(x)
    elif x > 2 and x <= 3.5:
        return 'Para x = ' + str(x) + ', f(x) = ' + str(2)
    elif x > 3.5 and x <= 5:
        return 'Para x = ' + str(x) + ', f(x) = ' + str(3)
    else:
        return 'Para x = ' + str(x) + ', f(x) = ' + str(x**2 - 10*x +28)

#Testes
# print(f_partes_exercicio(-1))
# print(f_partes_exercicio(0))
# print(f_partes_exercicio(2))
# print(f_partes_exercicio(3.5))
# print(f_partes_exercicio(5))
# print(f_partes_exercicio(6))


# 6 - Pacote para cálculo do salário líquido
# (a) Calcula o desconto segundo o INSS
def desc_inss(salario):
    '''Calcula o percentual de desconto aplicado ao salário informado de acordo com o INSS
    Entradas: salario (float)
    Saída: float'''

    if salario <= 2000:
        return salario * 0.06
    elif salario <= 3000:
        return salario * 0.08
    else:
        return salario * 0.1

#Testes
# print(desc_inss(1000.0))
# print(desc_inss(2000.0))
# print(desc_inss(3000.0))
# print(desc_inss(4000.00))

# (b) - Calcula o desconto segundo o IR
def desc_ir(salario):
    '''Calcula o percentual de desconto aplicado ao salário informado de acordo com o IR
    Entradas: salario (float)
    Saída: float'''

    if salario <= 2500:
        return salario * 0.11
    elif salario <= 5000:
        return salario * 0.15
    else:
        return salario * 0.22

#Testes
# print(desc_ir(1000.0))
# print(desc_ir(2500.0))
# print(desc_ir(5000.0))
# print(desc_ir(6000.0))

# (c) - Cálculo do Salário Líquido
def s_liquido(salario):
    '''Calcula o salário líquido a partir da informação do salário bruto, aplicando os descontos referentes ao INSS e IR
    Entradas: salario == (float)
    Saída: salário líquido == (float)'''

    return salario - (desc_inss(salario) + desc_ir(salario))

# #Testes
# print (s_liquido(1000))
# print (s_liquido(2000))
# print (s_liquido(2500))
# print (s_liquido(3000))
# print (s_liquido(5000))
# print (s_liquido(6000))