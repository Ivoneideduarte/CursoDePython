'''
frase = 'Curso de Python'

#Fatiamento
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])

print(frase.count('o')) #Conta a quantidade de vezes que a string 'o' aparece no texto
print(frase.upper().count('O')) #Conta a quant. de 'O' na frase jogada pra letra maiúscula
print(len(frase)) #Indica o tamanho da frase
print(len(frase.strip())) #O strip remove os espaços indesejados antes e depois da frase
print(frase.replace('Python', 'Android')) #Faz a troca de uma palavra por outra
print(frase[0])

frase = frase.replace('Python', 'Android')
print(frase)

print('Curso' in frase) #A palavra 'curso' existe dentro da frase?
print(frase.lower().find('Python')) #Verifica se existe a palavra dentro da frase e diz a posição dela

print(frase.split()) #Cria uma lista com separador de espaços
dividido = frase.split()
print(dividido)
print(dividido[0]) #Mosttra o primeiro item da lista
print(dividido[2][3])
'''

#Desafio 22
#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras no total(sem considerar espaços)
#Quantas letras tem o primeiro nome


nome = str(input('Digite seu nome completo: ')).strip() #Elimina os espaços antes e depois
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))