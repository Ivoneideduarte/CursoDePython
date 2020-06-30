#Desafio 06
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
from math import sqrt

n = float(input('Digite um valor: '))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)
print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz de {} é {}'.format(n, raiz))


