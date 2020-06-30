#Desafio 27

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome seoaradamente.
#Ex: Ivoneide Duarte dos Santos
#Primeiro: Ivoneide
#Último: Santos

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() #Este comando split() serve para fatiar uma palavra em pedaços
#print(nome) #Mostra a lista de caracteres
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0])) #Mosttra o primeiro item da lista
print('Seu último nome é {}'.format(nome[len(nome)-1])) #Com o comando len() posso saber quantas posições foram salvas na variável nome

