#Desafio 03
#Crie um programa que leia dois números e mostre a soma entre eles.

'''
Tipos primitivos
str()
int()
float()
bool()
'''

n1 = int(input('Digite um número: ')) #int() converte tudo que está dentro dele para o tipo inteiro
#print(type(n1)) #Mostra o tipo primitivo de n1, a classe dele é string por padrão
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))