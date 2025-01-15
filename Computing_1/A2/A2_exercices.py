# # Roteiro - Módulos Python

# # Módulo math
# import math                     # Importa todo o módulo math
# print(math.sqrt(81))

# from math import *              # Importa todo o módulo math
# print(sqrt(81))

# from math import sin            # Importa uma função específica do módulo math
# print(sin(3.14/2))


# # Ajuda com módulos
# help()                          # Abre um ambiente de explicação no terminal, só digitar o nome da biblioteca ou função





######################################### Laboratório A2 - Exercícios #########################################

#importando bibliotecas
from math import *

################## Cálculos Algébricos ##################

# 1 - Modularização
# (a) Testes no terminal
# max(3,2.8,3.9)
# min(7,2,4,1,0)


# (b) Media entre 3 números
def media_3(n1,n2,n3):
    '''Calcula a media entre 3 números fornecidos pelo usuário.
    Entradas:   n1 -> int
                n2 -> int
                n3 -> int
    Saída: float'''
    return fsum((n1,n2,n3))/3

#Testes
# print(media_3(1,2,3),media_3(0,9,3),media_3(0,0,0))

# (c)  Diferença do maior número com a média
def dif_maior_media(n1,n2,n3):
    '''Calcula a diferença do menor número com a média.
    Entradas:   n1 -> int
                n2 -> int
                n3 -> int
    Saída: float'''
    return max(n1,n2,n3) - media_3(n1,n2,n3)

#Testes
# print(dif_maior_media(1,2,3),dif_maior_media(0,9,3),dif_maior_media(0,0,0))

# (d)  Soma do menor número com a média
def soma_menor_media(n1,n2,n3):
    '''Calcula a diferença do menor número com a média.
    Entradas:   n1 -> int
                n2 -> int
                n3 -> int
    Saída: float'''
    return min(n1,n2,n3) + media_3(n1,n2,n3)

#Testes
# print(soma_menor_media(1,2,3),soma_menor_media(0,9,3),soma_menor_media(0,0,0))


# 2 - Função do 2°grau
# (a) Discriminante (delta)
def delta(a,b,c):
    '''Calcula o discriminante de uma função do segundo grau.
    Entradas:   coeficiente a -> int
                coeficiente b -> int
                coeficiente c -> int
    Saída: float'''
    return pow(b,2) - 4*a*c

#Testes
# print(delta(5,0,0),delta(1,4,0),delta(2,3,1),delta(4,4,2))

# (b) Primeira raiz
def x1(a,b,c):
    '''Calcula a primeira raiz de uma função do segundo grau.
    Entradas:   coeficiente a -> int
                coeficiente b -> int
                coeficiente c -> int
    Saída: float'''
    return (-b + sqrt(delta(a,b,c)))/(2*a)

#Testes
# print(x1(5,0,0), x1(1,4,0), x1(2,3,1))

# (c) Segunda raiz
def x2(a,b,c):
    '''Calcula a primeira raiz de uma função do segundo grau.
    Entradas:   coeficiente a -> int
                coeficiente b -> int
                coeficiente c -> int
    Saída: float'''
    return (-b - sqrt(delta(a,b,c)))/(2*a)

#Testes
# print(x2(5,0,0), x2(1,4,0), x2(2,3,1))


# 3 - Soma dos termos de uma P.A.
# (a) Número de termos de uma P.A.
def n_termos(a1,an,r):
    '''Calcula o número de termos de uma P.A.
    Entradas:   a1 -> primeiro termo [int]
                an -> ultimo termo [int]
                r -> razão da P.A. [int]
    Saída: float'''
    return 1 + (an-a1)//r

#Testes
# print(n_termos(1,10,1),n_termos(1,9,2))

# (b) Soma dos termos de uma P.A.
def soma_pa(a1,an,r):
    '''Calcula a soma dos termos de uma P.A.
    Entradas:   a1 -> primeiro termo [int]
                an -> ultimo termo [int]
                r -> razão da P.A. [int]
    Saída: float'''
    return (a1+an) * n_termos(a1,an,r)/2

#Testes
# print(soma_pa(1,10,1),soma_pa(1,9,2))         # Aqui tomar cuidado, pois eu que estou definindo o ultimo termo, tem que casar com a razão!


################## Cálculos Geométricos ##################

# 4 - Funções trigonométricas
# (a) - Distância entra dois pontos
def dist_2pontos(x1,y1,x2,y2):
    '''Calcula a distância entre dois pontos em um plano
    Entrada:    x1 - abscissa do ponto 1 [int]
                y1 - ordenada do ponto 1 [int]
                x2 - abscissa do ponto 2 [int]
                y2 - ordenada do ponto 2 [int]
    Saída:  float'''
    return dist((x1,y1),(x2,y2))

#Testes
# print(dist_2pontos(8,16,5,12),dist_2pontos(9,8,1,2),dist_2pontos(13,17,1,1))


# (b) - Perímetro de um triângulo
def perímetro_tri(x1,y1,x2,y2,x3,y3):
    '''Calcula o perímetro de um triângulo por meio da coordenada de seus vértices
    Entrada:    x1 - abscissa do ponto 1 [int]
                y1 - ordenada do ponto 1 [int]
                x2 - abscissa do ponto 2 [int]
                y2 - ordenada do ponto 2 [int]
                x3 - abscissa do ponto 3 [int]
                y3 - ordenada do ponto 3 [int]
    Saída:  float    '''
    return dist_2pontos(x1,y1,x2,y2) + dist_2pontos(x1,y1,x3,y3) + dist_2pontos(x2,y2,x3,y3)

#Testes
# print(perímetro_tri(8,16,5,12,8,12),perímetro_tri(9,8,1,2,9,2),perímetro_tri(13,17,1,1,13,1))

# (c) - relação fundamental trigonométrica
def rf_trigonometria(a):
    '''Comprovação da relação fundamental da trigonometria,, somando quadrado do seno com o quadrado do cosseno de um ângulo qualquer
    Entrada: a -> ângulo em graus [int]
    Saída: float'''
    return pow(sin(radians(a)),2) + pow(cos(radians(a)),2)

#Testes
# print(rf_trigonometria(30),rf_trigonometria(45),rf_trigonometria(60))   # Curioso o caso do 45


# 5 - Área do setor circular
def area_setor_circular(r,a=360):
    '''Calcula a área de um setor circular, dado o ângulo de abertura
    Entrada:    r -> raio do setor da circunferência
                a -> ângulo de abertura do setor em graus [int]
                Caso não seja informado o valor por padrão será 360°, ou seja, o círculo completo
    Saída: float'''
    return pi * pow(r,2) * a/360

#Testes
# print(area_setor_circular(1),area_setor_circular(1,180),area_setor_circular(2,90))