'''
nome = str(input('Qual é seu nome? '))
if nome == 'Ivoneide':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''

'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! Estude mais!')
'''

#Desafio 28

#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o úsuario tentar descobrir qual foi o número escolhiido pelo computador.
#O programa deverá escrever na tela se o úsuario venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5) #Faz o computador "PENSAR"
#print('Pensei no número {}'.format(computador))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2) #Espera por 2 segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))
