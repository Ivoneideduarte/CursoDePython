#Desafio 24
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).strip() #O comando strip, elimina os espaços indesejados
print(cidade[:5].upper() == 'SANTO')
