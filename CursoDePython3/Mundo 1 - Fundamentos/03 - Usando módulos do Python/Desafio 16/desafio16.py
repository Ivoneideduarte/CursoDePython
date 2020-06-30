#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e mostre o comp. da hipotenusa.

'''
print("======================== TRIÂNGULO RETÂNGULO ========================")
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
'''

'''
import math
print("======================== TRIÂNGULO RETÂNGULO ========================")
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
'''

from math import hypot
print("======================== TRIÂNGULO RETÂNGULO ========================")
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))