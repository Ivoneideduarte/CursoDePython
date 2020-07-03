# Desafio 33

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Verificando quem é o maior
if num1 > num2 and num1 > num3:
    print('O número 01 é Maior!')
if num2 > num1 and num2 > num3:
    print('O número 02 é Maior!')
if num3 > num1 and num3 > num2:
    print('O número 03 é Maior!')

#Verificando quem é o menor
if num1 < num2 and num1 < num3:
    print('O número 01 é Menor!')
if num2 < num1 and num2 < num3:
    print('O número 02 é Menor!')
if num3 < num1 and num3 < num2:
    print('O número 03 é Menor!')
'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
